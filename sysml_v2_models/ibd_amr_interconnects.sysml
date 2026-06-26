package ibd_amr_interconnects {
    doc
    /*
     * IBD: Internal Block Diagram modeling the interconnects
     * between AMR parts (data and power flows).
     */
     
    import bdd_amr_architecture::*;

    part def AMR_Platform :> AutonomousMobileRobot {
        // Instantiate parts inside the platform
        part mainComputer : ComputeNode;
        part perceptionSensors : SensorSuite;
        part driveController : MotorController;
        part powerSystem : PowerDistributionUnit;

        // Internal connections (Ports and Connections)
        connect perceptionSensors.data_tx to mainComputer.ethernetPort_in;
        connect mainComputer.ethernetPort_out to driveController.command_rx;
        connect powerSystem.power_tx to driveController.power_rx;
    }
}
