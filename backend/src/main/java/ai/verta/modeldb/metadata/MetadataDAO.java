package ai.verta.modeldb.metadata;

import ai.verta.common.OperatorEnum;
import ai.verta.modeldb.ModelDBException;
import java.util.List;

public interface MetadataDAO {
  boolean addLabels(IdentificationType id, List<String> labels);

  boolean updateLabels(IdentificationType id, List<String> labels) throws ModelDBException;

  List<String> getLabels(IdentificationType id);

  List<IdentificationType> getLabelIds(List<String> labels, OperatorEnum.Operator operator);

  boolean deleteLabels(IdentificationType id, List<String> labels, boolean deleteAll);
}
