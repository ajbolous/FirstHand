using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApplication6
{
    public class Sensor
    {
        public int distance;
        public SerialPort sp;

        public Sensor(string port, int baud)
        {

            ///HERE WE WANT TO CREATE THE SERIAL PORT, THE EVENT HANDLERS ..
            /// 

            sp = new SerialPort(port, baud);
            
                sp.DataReceived += Sp_DataReceived;
        }

        private void Sp_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            string line = sp.ReadLine();
            int dist = -1;
            int.TryParse(line, out dist);
            if (dist != -1)
            {
                distance = dist;

            }

          }

        public int getDistance()
        {
            return distance;
        }

       



    }
}
