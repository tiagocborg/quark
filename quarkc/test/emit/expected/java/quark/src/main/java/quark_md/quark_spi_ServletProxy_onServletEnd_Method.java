package quark_md;

public class quark_spi_ServletProxy_onServletEnd_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public quark_spi_ServletProxy_onServletEnd_Method() {
        super("quark.void", "onServletEnd", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.String"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        quark.spi.ServletProxy obj = (quark.spi.ServletProxy) (object);
        (obj).onServletEnd((String) ((args).get(0)));
        return null;
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}
