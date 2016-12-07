# Copyright 2015 datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .match import match, choice
from .tree import walk_dfs
from .ir import (IR, Root, Namespace, Definition, Class, TestClass,
                 Declaration, Check, TestMethod, Method,
                 PublicDeclaration, LocalDeclaration)
from .emit_target import Target, Ruby, Go
from .emit_ir import Snowflake


@match(Root, Target)
def rename(root, target):
    """ Define a target name for each definition and namespace """
    assert target.q is not None, "Need a target from target.with_root(root)"
    for pkg in root.children:
        for node in walk_dfs(pkg):
            rename(node, target)

@match(IR, Target)
def rename(node, target):
    pass

@match(choice(Namespace, Definition), Target)
def rename(ns, target):
    rename(ns, ns.name.path[-1], target)

@match(choice(Namespace,Definition,Declaration,Method), basestring, Target)
def rename(ns, name, target):
    target.define_name(ns.name, name)

@match(IR, Snowflake, Target)
def rename(named, name, target):
    assert False, "Unhandled special case %r" % named.name

@match(Definition, Go)
def rename(dfn, target):
    target.define_name(dfn.name, target.upcase("_".join(dfn.name.path[1:])))

@match(Namespace, Snowflake("test"), Go)
def rename(ns, name, target):
    rename(ns, "{pkg}_test".format(
        pkg = target.nameof(target.q.parent(ns))),
           target)


@match(choice(PublicDeclaration,Method), Target)
def rename(decl, target):
    rename(decl, target.varname(decl.name), target)

@match(LocalDeclaration, Target)
def rename(decl, target):
    rename(decl, target.varname(decl.name), target)

@match(choice(PublicDeclaration,Method), Go)
def rename(decl, target):
    rename(decl, target.upcase(decl.name), target)

@match(Check, Go)
def rename(dfn, target):
    rename(dfn, "TestQ_{name}".format(
        name="_".join(dfn.name.path[1:])),
           target)

@match(TestMethod, Go)
def rename(dfn, target):
    rename(dfn, "TestQ_{klass}_{name}".format(
        klass = target.nameof(target.q.parent(dfn)),
        name = target.upcase(dfn.name.name)),
           target)

@match(Class, Ruby)
def rename(dfn, target):
    rename(dfn, target.upcase(dfn.name.path[-1]), target)

@match(TestClass, Ruby)
def rename(dfn, target):
    rename(dfn, "Test" + target.upcase(dfn.name.path[-1]), target)
