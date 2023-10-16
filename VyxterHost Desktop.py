import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una vista web
        self.browser = QWebEngineView(self)

        # Establecer un agente de usuario personalizado
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.browser.page().profile().setHttpUserAgent(user_agent)

        # Habilitar JavaScript en la vista web
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        # Obtener el perfil de la página web
        profile = self.browser.page().profile()

        # Habilitar cookies en el perfil
        profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)

        # Cargar el enlace proporcionado
        twitch_embed_url = "https://panel.vyxterhost.com/"
        self.browser.setUrl(QUrl(twitch_embed_url))

        # Ocultar la barra de herramientas y la barra de direcciones
        self.browser.setContextMenuPolicy(Qt.NoContextMenu)

        # Configurar la ventana principal
        self.setCentralWidget(self.browser)
        self.setWindowTitle("VyxterHost")

        # Crear un menú personalizado para cerrar la ventana
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("⚙| Opciones")

        # Agregar botones de retroceso y avance al menú "Opciones"
        back_action = QAction("🢀| Retroceder", self)
        back_action.triggered.connect(self.browser.back)
        menu.addAction(back_action)

        forward_action = QAction("🢂| Avanzar", self)
        forward_action.triggered.connect(self.browser.forward)
        menu.addAction(forward_action)

        # Agregar un botón "Soporte"
        go_to_action = QAction("☎| Soporte", self)
        go_to_action.triggered.connect(self.go_to_soporte)
        menu.addAction(go_to_action)

        # Agregar una opción para cerrar la ventana
        close_action = QAction("✖| Cerrar Vyxterhost", self)
        close_action.triggered.connect(self.close)
        menu.addAction(close_action)

    def go_to_soporte(self):
        # Redirigir a la URL de Soporte
        soporte_url = "https://panel.vyxterhost.com/tickets"
        self.browser.setUrl(QUrl(soporte_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.showFullScreen()  # Mostrar la ventana en pantalla completa
    sys.exit(app.exec_())
