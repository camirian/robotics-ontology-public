package pkg_amr_decomposition {
    doc
    /*
     * Structural Decomposition: Demonstrating the 
     * Package -> Block -> Part -> Port hierarchy.
     */

    import bdd_amr_architecture::*;
    import ibd_amr_interconnects::*;

    package AMR_System {
        // The top-level system part, establishing the root of our hierarchy
        part primaryAMR : AMR_Platform {
            /* 
             * Nested part redefinitions to showcase deep hierarchy 
             */
            part redefines mainComputer {
                port redefines ethernetPort_in;
                port redefines ethernetPort_out;
            }
            part redefines perceptionSensors {
                port redefines data_tx;
            }
            part redefines driveController {
                port redefines command_rx;
                port redefines power_rx;
            }
            part redefines powerSystem {
                port redefines power_tx;
            }
        }
    }
}
