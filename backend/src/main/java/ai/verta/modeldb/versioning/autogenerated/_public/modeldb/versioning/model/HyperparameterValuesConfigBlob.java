// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;

public class HyperparameterValuesConfigBlob {
    public Long IntValue;
    public Float FloatValue;
    public String StringValue;

    public HyperparameterValuesConfigBlob() {
        this.IntValue = 0l;
        this.FloatValue = 0.f;
        this.StringValue = null;
    }

    public HyperparameterValuesConfigBlob setIntValue(Long value) {
        this.IntValue = value;
        return this;
    }
    public HyperparameterValuesConfigBlob setFloatValue(Float value) {
        this.FloatValue = value;
        return this;
    }
    public HyperparameterValuesConfigBlob setStringValue(String value) {
        this.StringValue = value;
        return this;
    }

    static public HyperparameterValuesConfigBlob fromProto(ai.verta.modeldb.versioning.HyperparameterValuesConfigBlob blob) {
        HyperparameterValuesConfigBlob obj = new HyperparameterValuesConfigBlob();
        {
            Function<ai.verta.modeldb.versioning.HyperparameterValuesConfigBlob,Long> f = x -> { return (x.getIntValue()); };
            //;
            if (f != null) {
                obj.IntValue = f.apply(blob);
            }
        }
        {
            Function<ai.verta.modeldb.versioning.HyperparameterValuesConfigBlob,Float> f = x -> { return (x.getFloatValue()); };
            //;
            if (f != null) {
                obj.FloatValue = f.apply(blob);
            }
        }
        {
            Function<ai.verta.modeldb.versioning.HyperparameterValuesConfigBlob,String> f = x -> { return (x.getStringValue()); };
            //;
            if (f != null) {
                obj.StringValue = f.apply(blob);
            }
        }
        return obj;
    }

    public void preVisitShallow(Visitor visitor) throws ModelDBException {
        visitor.preVisitHyperparameterValuesConfigBlob(this);
    }

    public void preVisitDeep(Visitor visitor) throws ModelDBException {
        this.preVisitShallow(visitor);
        visitor.preVisitDeepLong(this.IntValue);
        visitor.preVisitDeepFloat(this.FloatValue);
        visitor.preVisitDeepString(this.StringValue);
    }

    public HyperparameterValuesConfigBlob postVisitShallow(Visitor visitor) throws ModelDBException {
        return visitor.postVisitHyperparameterValuesConfigBlob(this);
    }

    public HyperparameterValuesConfigBlob postVisitDeep(Visitor visitor) throws ModelDBException {
        this.IntValue = visitor.postVisitDeepLong(this.IntValue);
        this.FloatValue = visitor.postVisitDeepFloat(this.FloatValue);
        this.StringValue = visitor.postVisitDeepString(this.StringValue);
        return this.postVisitShallow(visitor);
    }
}