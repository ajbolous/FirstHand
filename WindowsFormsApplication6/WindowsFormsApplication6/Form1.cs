using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Media;
using System.IO.Ports;
using System.Timers;

namespace WindowsFormsApplication6
{
    public partial class Form1 : Form
    {
        private  System.Timers.Timer aTimer;
        public SoundPlayer simpleSound;
        SerialPort mySerialPort = new SerialPort("COM3");


        public Form1()
        {

            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            aTimer = new System.Timers.Timer(500);
            mySerialPort.BaudRate = 9600;
            simpleSound = new SoundPlayer(@"c:\Windows\Media\chimes.wav");

            mySerialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);

            mySerialPort.Open();

            aTimer.Elapsed += ATimer_Elapsed;

        }

        private void DataReceivedHandler(
                            object sender,
                            SerialDataReceivedEventArgs e)
        {
           
            
            
            string indata = mySerialPort.ReadLine();
          int x = int.Parse(indata);
            if (x == -1)
                x = 10;
            if (x < 20)
                aTimer.Interval = 50 * x;
                aTimer.Start();
                
            if (x > 20)
                aTimer.Stop();
                this.Invoke((MethodInvoker)delegate
            {
                listBox1.Items.Add(indata);
            });

        }

        private void ATimer_Elapsed(object sender, ElapsedEventArgs e)
        {
            
                simpleSound.Play();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Disconnect_Click(object sender, EventArgs e)
        {
            mySerialPort.Close();

        }

    }

}
