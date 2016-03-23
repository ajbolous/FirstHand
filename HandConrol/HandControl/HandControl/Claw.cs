using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HandControl
{
    class Claw
    {
        public Servo servo;
        public Claw()
        {
            //manteqe?aaaa hhh good wen bdna ne3ml al gui i3ne manzar al2ed 3d >?
            ///bedna nst3mel openGL ele nrsem
            /// tyb bs msh c# hdek c
            /// fee opengl lal c# its the same bs hdek bdon form 3l consol sawenaha
            /// fee eshya tanye max ele kaman hwayne 
            /// ok
            /// 
        }
        public void Close()
        {
            servo.SetAngle(0);
        }
        public void Open()
        {
            servo.SetAngle(180);
        }
    }
}
