package bdd_amr_architecture {
    doc
    /*
     * BDD: Block Definition Diagram modeling the basic AMR components.
     * Demonstrating SysML v2 syntax for definition of components.
     */

    import ScalarValues::*;

    part def ComputeNode {
        attribute cpuCores : Integer;
        attribute ramGB : Real;
        port ethernetPort_in;
        port ethernetPort_out;
    }

    part def SensorSuite {
        attribute lidarRange_m : Real;
        attribute cameraResolution_MP : Real;
        port data_tx;
    }

    part def MotorController {
        attribute maxVoltage_V : Real;
        attribute peakCurrent_A : Real;
        port command_rx;
        port power_rx;
        port phase_drive_tx;
    }

    part def PowerDistributionUnit {
        attribute batteryCapacity_Ah : Real;
        port power_tx;
    }
    
    // Abstract supertype for any Autonomous Mobile Robot
    part def AutonomousMobileRobot;
}
