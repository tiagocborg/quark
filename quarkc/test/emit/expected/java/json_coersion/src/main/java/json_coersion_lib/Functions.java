package json_coersion_lib;

public class Functions {
    public static void main() {
        io.datawire.quark.runtime.JSONObject json = new io.datawire.quark.runtime.JSONObject();
        (json).setObjectItem(("string"), ((new io.datawire.quark.runtime.JSONObject()).setString("this is a string")));
        (json).setObjectItem(("number"), ((new io.datawire.quark.runtime.JSONObject()).setNumber(3.14159)));
        (json).setObjectItem(("boolean"), ((new io.datawire.quark.runtime.JSONObject()).setBool(true)));
        String encoded = (json).toString();
        do{System.out.println(encoded);System.out.flush();}while(false);
        io.datawire.quark.runtime.JSONObject dec = io.datawire.quark.runtime.JSONObject.parse(encoded);
        String string = ((dec).getObjectItem("string")).getString();
        Double number = ((dec).getObjectItem("number")).getNumber();
        Boolean boolean_ = ((dec).getObjectItem("boolean")).getBool();
        do{System.out.println(string);System.out.flush();}while(false);
        do{System.out.println(number);System.out.flush();}while(false);
        do{System.out.println((boolean_).toString());System.out.flush();}while(false);
    }
}