# GEMINI.md
This file provides guidance to GEMINI when working with code in this repository.

## Commonly Used Commands

*   **Run the development server:**
    ```bash
    ./runserver.sh
    ```
*   **Run tests:**
    ```bash
    ./test.sh
    ```
*   **Run a single test:**
    ```bash
    python manage.py test reversi.tests.test_views.ViewsTest.test_index
    ```

## High-level Code Architecture

This is a Django-based Reversi game. The core game logic is implemented in Python and the front end is built with HTML, CSS, and JavaScript.

*   **Backend:** The backend is a Django application located in the `reversi` directory.
    *   `views.py`: This file contains the main application logic. It handles requests from the front end, manages the game state stored in the session, and returns JSON responses.
    *   `models.py`: This file is currently empty. The game state is not stored in a database.
    *   `urls.py`: This file defines the URL patterns for the application.
*   **Frontend:** The frontend consists of HTML, CSS, and JavaScript files located in the `templates` and `static` directories.
    *   `templates/reversi/index.html`: This is the main HTML file for the game.
    *   `static/reversi/css/`: This directory contains the CSS files for the game.
    *   `static/reversi/js/`: This directory contains the JavaScript files for the game.
*   **Game Logic:** The core Reversi game logic is implemented in the `reversi/model/` directory.
    *   `ReversiPlay.py`: This class manages the game play, including player moves and CPU moves.
    *   `Reversi.py`: This class represents the Reversi board and contains the core game logic.
    *   `ReversiHistory.py`: This class stores the history of the game.
    *   `ReversiSetting.py`: This class manages the game settings.

## Usage Notes

*   The game state is stored in the user's session. There is no database used in this application.
*   The application uses a front controller pattern, where all requests are handled by the `frontController` and `frontControllerS` functions in `views.py`.
*   The communication between the front end and the back end is done via AJAX requests and JSON responses.
