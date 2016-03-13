using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HandControl
{
    class Servo
    {//Variables are small letters
        int angle = 0; //Servo only rotates between 0- 180 * asa bdna r2am al servo syaes7 yes
        int servoId;
        public int GetAngle()
        {
            return angle;
        }
        public bool SetAngle(int angle)
        {
            if (angle > 0 && angle < 180)
            {
                this.angle = angle;
                return true;
            }
            return false;
        }
    }
}
