#include "../include/raylib.h"
// #include "../include/raymath.h"
#include <stdio.h>

struct Ball {

  float x, y;
  float speed_x, speed_y;
  float radius;

  void Draw() { DrawCircle((int)x, (int)y, radius, WHITE); }
};

struct Paddle {

  float x, y;
  float speed;
  float width, height;

  void Draw() { DrawRectangle(x - width / 2, y - height / 2, 10, 100, WHITE); }
};

int main() {
  int width{800};
  int height{600};
  bool running{true};
  SetExitKey(0);

  InitWindow(width, height, "Pong");
  SetWindowState(FLAG_VSYNC_HINT);

  Ball ball;
  ball.x = GetScreenWidth() / 2.0f;
  ball.y = GetScreenHeight() / 2.0f;
  ball.radius = 5;
  ball.speed_x = 100;
  ball.speed_y = 300;

  Paddle left_paddle;
  left_paddle.x = 50;
  left_paddle.y = GetScreenHeight() / 2.0f;
  left_paddle.width = 10;
  left_paddle.height = 100;
  left_paddle.speed = 500;

  Paddle right_paddle;
  left_paddle.x = 50;
  left_paddle.y = GetScreenHeight() / 2.0f;
  left_paddle.width = 10;
  left_paddle.height = 100;
  left_paddle.speed = 500;

  while (running) {

    if (IsKeyPressed(0) || WindowShouldClose())
      running = false;

    ball.x += ball.speed_x * GetFrameTime();
    ball.y += ball.speed_y * GetFrameTime();

    if (ball.y < 0) {
      ball.y = 0;
      ball.speed_y *= -1;
    }
    if (ball.y > GetScreenHeight()) {
      ball.y = GetScreenHeight();
      ball.speed_y *= -1;
    }

    BeginDrawing();
    ClearBackground(BLACK);

    ball.Draw();
    DrawRectangle(50, GetScreenHeight() / 2 - 50, 10, 100, WHITE);
    DrawRectangle(GetScreenWidth() - 50 - 10, GetScreenHeight() / 2 - 50, 10,
                  100, WHITE);

    DrawFPS(10, 10);
    EndDrawing();
  }
  CloseWindow();

  return 0;
}
