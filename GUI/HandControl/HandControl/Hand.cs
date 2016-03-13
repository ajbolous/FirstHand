using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HandControl
{
    class Hand
    {
        public List<Axis> axis = new List<Axis>();
        // hay list, zay ma3ra7' dynamic... ele b3'dar azed 3ali items o22em.. zay reshema mekosheret
        //btw 7'aale el comments hek bttzkre.
        //grip=1 if the claw is open else it's zero
        public Claw claw;

        public void Move(int[] angles, bool grip) 
            
            {
            for (int i = 0; i < 5; i++)
                axis[i].servo.SetAngle(angles[i]);
            if (grip == false)
                claw.Close();
            else
                claw.Open();
            }



    }
}
