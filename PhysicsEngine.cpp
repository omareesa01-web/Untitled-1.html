// كود C++ لحساب فيزياء الجاذبية والاصطدام بسرعة فائقة (High Performance)
#include <iostream>

struct Player {
    float x, y;
    float velY;
};

void applyGravity(Player& p, float gravityConst) {
    p.velY += gravityConst;
    p.y += p.velY;
    
    // منع اللاعب من السقوط تحت الأرض (حد الأرضية 350)
    if (p.y >= 300) {
        p.y = 300;
        p.velY = 0;
    }
}

int main() {
    std::cout << "C++ Physics Engine Initialized Successfully." << std::endl;
    return 0;
}
