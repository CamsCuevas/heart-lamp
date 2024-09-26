void setup() {
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char receivedChar = Serial.read();
    if (receivedChar == '1') {
      digitalWrite(8, HIGH); 
    } else if (receivedChar == '0') {
      digitalWrite(8, LOW);
    }
  }
}
