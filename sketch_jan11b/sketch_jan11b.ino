
int b1 = 2;
int b2 = 4;
int b3 = 7;
int b4 = 8;
int b5 = 12;

int p1 = 10; // player 1
int p2 = 11; // player 2
int turn = 0;
int column, win;

void setup() {
  pinMode(b1, INPUT);
  pinMode(b2, INPUT);
  pinMode(b3, INPUT);
  pinMode(b4, INPUT);
  pinMode(b5, INPUT);
  
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);

  Serial.begin(9600);

  for (int i = 0; i < 6; i++) {
    digitalWrite(p2, LOW);
    digitalWrite(p1, HIGH);
    delay(250);
    digitalWrite(p1, LOW);
    digitalWrite(p2, HIGH);
    delay(250);
  }
}

void loop() {

  digitalWrite(p1, LOW);
  digitalWrite(p2, LOW);
  
  switch (turn) {

    case 0:

      digitalWrite(p1, HIGH);

      while (true) {
        if (digitalRead(b1) == 1) {
          Serial.println(1);
          delay(1000);
          break;
        }

        if (digitalRead(b2) == 1) {
          Serial.println(2);
          delay(1000);
          break;
        }

        if (digitalRead(b3) == 1) {
          Serial.println(3);
          delay(1000);
          break;
        }

        if (digitalRead(b4) == 1) {
          Serial.println(4);
          delay(1000);
          break;
        }

        if (digitalRead(b5) == 1) {
          Serial.println(5);
          delay(1000);
          break;
        }
        
      }

      digitalWrite(p1, LOW);

      turn = 1;
      break;
      
    case 1:

      digitalWrite(p2, HIGH);
      delay(500);
      digitalWrite(p2, LOW);

      turn = 0;
      break;
  }
}
