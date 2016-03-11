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
        //Here we declare the variables we are going to use
        private  System.Timers.Timer aTimer;
        public SoundPlayer simpleSound;
        SerialPort mySerialPort;

        //Constructors
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Allocate new OBJECTS , using new
            aTimer = new System.Timers.Timer(500);
            mySerialPort = new SerialPort("COM3",9600);
            simpleSound = new SoundPlayer(@"c:\Windows\Media\chimes.wav");
            //Attach handlers to events
            mySerialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);
            aTimer.Elapsed += ATimer_Elapsed;
            //Start serialport and reading data
            mySerialPort.Open();

        }

        private void DataReceivedHandler(object sender,SerialDataReceivedEventArgs e)
        {
          string indata = mySerialPort.ReadLine();
          int distance = int.Parse(indata);

            if (distance == -1)
                distance = 10;
            if (distance < 20)
            {
                aTimer.Interval = 50 * distance;
                aTimer.Start();
            }
                ///ahdab
            if (distance > 20)
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
