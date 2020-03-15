// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;

public class S3DatasetComponentBlob {
    public PathDatasetComponentBlob Path;

    public S3DatasetComponentBlob() {
        this.Path = null;
    }

    public S3DatasetComponentBlob setPath(PathDatasetComponentBlob value) {
        this.Path = value;
        return this;
    }

    static public S3DatasetComponentBlob fromProto(ai.verta.modeldb.versioning.S3DatasetComponentBlob blob) {
        S3DatasetComponentBlob obj = new S3DatasetComponentBlob();
        {
            Function<ai.verta.modeldb.versioning.S3DatasetComponentBlob,PathDatasetComponentBlob> f = x -> { return PathDatasetComponentBlob.fromProto(x.getPath()); };
            //PathDatasetComponentBlob.fromProto;
            if (f != null) {
                obj.Path = f.apply(blob);
            }
        }
        return obj;
    }

    public void preVisitShallow(Visitor visitor) throws ModelDBException {
        visitor.preVisitS3DatasetComponentBlob(this);
    }

    public void preVisitDeep(Visitor visitor) throws ModelDBException {
        this.preVisitShallow(visitor);
        visitor.preVisitDeepPathDatasetComponentBlob(this.Path);
    }

    public S3DatasetComponentBlob postVisitShallow(Visitor visitor) throws ModelDBException {
        return visitor.postVisitS3DatasetComponentBlob(this);
    }

    public S3DatasetComponentBlob postVisitDeep(Visitor visitor) throws ModelDBException {
        this.Path = visitor.postVisitDeepPathDatasetComponentBlob(this.Path);
        return this.postVisitShallow(visitor);
    }
}