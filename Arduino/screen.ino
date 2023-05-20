
#define TFT_DC    7
#define TFT_RST   8 
#define SCR_WD   240
#define SCR_HT   240   // 320 - to allow access to full 240x320 frame buffer
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Arduino_ST7789_Fast.h>
#include<Chrono.h>
//#include<time.h>
Arduino_ST7789 lcd = Arduino_ST7789(TFT_DC, TFT_RST);

bool startbut = false; // флаг для кнопки старта
bool countbut = false; // флаг для кнопки процентов
int countstate = 0;    // чтение LOW или HIGH
int startstate = 0;    // чтение LOW или HIGH
uint16_t percent = 0;  // проценты не воды
uint16_t v = 200;      // объем напитка

Chrono clap_chrono;             // объявление таймера 
bool clap_chrono_start = false; // флаг работы таймера

 
void setup(void) 
{
  Serial.begin(115200);
  lcd.init(SCR_WD, SCR_HT);
  lcd.fillScreen(BLACK);
  pinMode(A1, OUTPUT);  // сигнал 1 на реле  
  pinMode(A2, OUTPUT);  // сигнал 2 на реле (вода)
  pinMode(A4, OUTPUT);  // кнопка старта
  pinMode(A5, OUTPUT);  // кнопка ввода процентов
  digitalWrite(A1, HIGH);
  digitalWrite(A2, HIGH);
  digitalWrite(A4, HIGH);
  digitalWrite(A5, HIGH);
  lcd.setCursor(0, 0);
  lcd.setTextColor(WHITE,BLACK);
  lcd.setTextSize(9);

  clap_chrono.stop();
 }

void clapwork(uint16_t percent, uint16_t v)
{
  double t1 = v * (100 - percent) / 510 ;                  // для воды, с
  double t2 = v *  percent / 450 ;                         // для газировки, с

  bool work = true;  // работает цикл
  bool A1_on = true; // работает клапан A1
  bool A2_on = true; // работает клапан A2

  clap_chrono_start = true;
  clap_chrono.restart();
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  while(work)
  {
    if(clap_chrono.hasPassed(t1*1000) && A1_on)
    {
      digitalWrite(A1, HIGH);
     // Serial.print("A1 stop after ");
     // Serial.print(clap_chrono.elapsed());
     // Serial.println(" ms");
      A1_on = false;
    }
    if(clap_chrono.hasPassed(t2*1000) && A2_on)
    {
      digitalWrite(A2, HIGH);
    //  Serial.print("A2 stop after ");
    // Serial.print(clap_chrono.elapsed());
    // Serial.println(" ms");
      A2_on = false;
    }
    
    if(!A1_on && !A2_on)
    {
      work = false;
      clap_chrono.stop();
      clap_chrono_start = false;
    }
  }
  digitalWrite(A1, HIGH);
  digitalWrite(A2, HIGH);
}

void loop()
{
  countstate = digitalRead(A5);
  if(countbut == false && countstate == 0)
  {
    delay(30);
    countstate = digitalRead(A5);
    if(countstate == 0)
    {
      countbut = true;   
      percent += 5;
      if(percent == 100)
      {
        percent = 0;
      }
      lcd.clearScreen();
      lcd.setCursor(0, 0);
      lcd.println(percent);
    }
  }
  if(countbut == true && countstate == 1)
  {
    delay(30);
    countstate = digitalRead(A5);
    if(countstate == 1)
    {
      countbut = false;
    }
  } 
  startstate = digitalRead(A4);
  if(startbut == false && startstate == 0)
  {
    delay(30);
    startstate = digitalRead(A4);
    if(startstate == 0)
    {
      startbut = true;
      if(percent == 0 || percent == 5)
      {
        Serial.print(0);
      }
      Serial.print(percent);
      clapwork(percent, v);
      percent = 0;
      lcd.clearScreen();
      lcd.setCursor(0, 0);
      lcd.println(percent);  
    }
  }
  if(startbut == true && startstate == 1)
  {
    delay(30);
    startstate = digitalRead(A4);
    if(startstate == 1)
    {
      startbut = false;
    }
  } 
}
