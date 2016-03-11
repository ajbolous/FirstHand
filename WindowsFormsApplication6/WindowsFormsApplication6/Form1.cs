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
       private static System.Timers.Timer aTimer;
       
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
           

            mySerialPort.BaudRate = 9600;
           // SoundPlayer simpleSound = new SoundPlayer(@"c:\Windows\Media\chimes.wav");

            mySerialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);

            mySerialPort.Open(); 
             
            //simpleSound.Play(); 
            
        }

        private void DataReceivedHandler(
                            object sender,
                            SerialDataReceivedEventArgs e)
        {
            SoundPlayer simpleSound = new SoundPlayer(@"c:\Windows\Media\chimes.wav");
            int x;
            
            aTimer = new System.Timers.Timer(5);
            aTimer.Elapsed += OnTimedEvent;//to do
            string indata = mySerialPort.ReadLine();
            x = int.Parse(indata);
            if (x<20)
                simpleSound.Play();
            this.Invoke((MethodInvoker)delegate
            {
                listBox1.Items.Add(indata);
            });

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
