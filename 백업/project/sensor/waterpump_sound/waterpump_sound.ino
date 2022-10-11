int water_pin = A0;      //수분수위센서 A0에 연결
int pumpAA = 7;
int pumpAB = 6;
int sound = A1;          //사운드센서 A1에 연결

void setup() {
  Serial.begin(9600);    
  pinMode(pumpAA, OUTPUT);
  pinMode(pumpAB, OUTPUT);
  
}

void loop(){
  int water_val = analogRead(A0);   // 수분수위센서값을 'water_val'에 저장 
  int sound_val = analogRead(A1);   // 사운드센서값을 'sound_val'에 저장
  Serial.print("wt:");
  Serial.println(water_val);
  if(Serial.available()>0){
    String data = Serial.readString();
    if (data == "open"){
      Serial.print("arduino waterpumping");
      digitalWrite(pumpAA, HIGH);
      digitalWrite(pumpAB, LOW);
      delay(3000);
      digitalWrite(pumpAA, LOW);
      digitalWrite(pumpAB, LOW);
      }
  }else if(water_val < 400){
  digitalWrite(pumpAA, HIGH);
  digitalWrite(pumpAB, LOW);
  delay(3000);
  digitalWrite(pumpAA, LOW);
  digitalWrite(pumpAB, LOW);
  }
 delay(500);
}
