# default_enums.py
# This script contains default values for enums classes to use when instanciating a Farm with create_farm function
from pyholos.farm.enums import (CarbonModellingStrategies,
                                ChosenClimateAcquisition,
                                ResidueInputCalculationMethod,
                                SoilDataAcquisitionMethod,
                                YieldAssignmentMethod)


class DefaultEnums:
    ResidueInputCalculationMethod = ResidueInputCalculationMethod.Default
    SoilDataAcquisitionMethod = SoilDataAcquisitionMethod.Default
    ChosenClimateAcquisition = ChosenClimateAcquisition.NASA
    YieldAssignmentMethod = YieldAssignmentMethod.SmallAreaData
    CarbonModellingStrategies = CarbonModellingStrategies.ICBM
