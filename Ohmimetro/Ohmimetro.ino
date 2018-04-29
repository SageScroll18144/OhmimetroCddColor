double r1;
double r2 = 2200;
double x;
void setup() {Serial.begin(9600);}

void loop() { 
  x = analogRead(A0)*0.0048828125;
  
  r1 = (5*r2/x)-r2;
  Serial.print("Valor do resistor medido  : ");
  if(analogRead(A0)<=0){
    Serial.println("Ponha um resistor para ser medido..."); 
  }else if(r1>=1000){
    Serial.print(r1/1000);
    Serial.println("  K Ohms"); 
  }else{
    Serial.print(r1);
    Serial.println("  Ohms");
  }
  delay(1000);
}

