#include <iostream>
using namespace std;

class Rectangle {
protected:
  int width;
  int height;

public:
  void setwidth(int width) { this->width = width; }
  void setheight(int height) { this->height = height; }
  virtual void display() const { cout << width << ' ' << height << endl; }
};

class RectangleArea : public Rectangle {
public:
  void display() const override { cout << (width * height) << endl; }
  void read_input() { cin >> width >> height; }
};
