#include <SFML/Graphics.hpp>

class Player {
public:
    sf::RectangleShape shape;
    sf::Vector2f velocity;
    float speed;

    Player(sf::Vector2f size, sf::Vector2f position) {
        shape.setSize(size);
        shape.setPosition(position);
        shape.setFillColor(sf::Color::Green);
        speed = 5.f;
    }

    void update() {
        shape.move(velocity);
    }

    void draw(sf::RenderWindow& window) {
        window.draw(shape);
    }
};

class Game {
public:
    sf::RenderWindow window;
    Player player;

    Game() : window(sf::VideoMode(800, 600), "Platformer Game"), player(sf::Vector2f(50.f, 50.f), sf::Vector2f(100.f, 100.f)) {
        window.setFramerateLimit(60);
    }

    void run() {
        while (window.isOpen()) {
            sf::Event event;
            while (window.pollEvent(event)) {
                if (event.type == sf::Event::Closed)
                    window.close();
            }

            handleInput();
            update();
            render();
        }
    }

    void handleInput() {
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            player.velocity.x = -player.speed;
        else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            player.velocity.x = player.speed;
        else
            player.velocity.x = 0.f;

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space))
            player.velocity.y = -10.f; // Jump

        // Add gravity
        player.velocity.y += 0.5f;

        // Limit the velocity
        if (player.velocity.y > 10.f)
            player.velocity.y = 10.f;
    }

    void update() {
        player.update();

        // Collision with window bounds
        if (player.shape.getPosition().x < 0)
            player.shape.setPosition(0, player.shape.getPosition().y);
        if (player.shape.getPosition().x + player.shape.getSize().x > window.getSize().x)
            player.shape.setPosition(window.getSize().x - player.shape.getSize().x, player.shape.getPosition().y);
        if (player.shape.getPosition().y + player.shape.getSize().y > window.getSize().y)
            player.shape.setPosition(player.shape.getPosition().x, window.getSize().y - player.shape.getSize().y);
    }

    void render() {
        window.clear();
        player.draw(window);
        window.display();
    }
};

int main() {
    Game game;
    game.run();
    return 0;
}
