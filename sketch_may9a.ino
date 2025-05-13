int const inf_sensorPin = A0;
int const trigPin= 13;
int const echoPin= 12;
float Ult_Duration,Ult_Distance,inf_Distance;
const int BUTTON_PIN = 7;
int buttonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
  digitalWrite(trigPin,LOW);
  
}

void loop() {
  // inf_Distance = analogRead(inf_sensorPin); 
  // Serial.println(inf_Distance);
  buttonState = digitalRead(BUTTON_PIN);
  if(buttonState == LOW){
    digitalWrite(trigPin,HIGH); 
    digitalWrite(trigPin,LOW);
    Ult_Duration = pulseIn(echoPin,HIGH); 
    Ult_Distance = Ult_Duration*0.034/2; 
    Serial.println(Ult_Distance);
  }else{
    Serial.println(0);
  }
  delay(200);
}
