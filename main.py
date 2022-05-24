import sys
from PyQt5.QtWidgets import QApplication
from backend.logica_juego import Froggie
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from backend.logica_ranking import LogicaRanking
from frontend.VentanaLogIn import VentanaLogIn
from frontend.VentanaRanking import VentanaRanking
from frontend.VentanaJuego import VentanaJuego
from frontend.VentanaPostnivel import VentanaPostnivel
import parametros as p

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])


    ventana_inicio = VentanaLogIn()
    ventana_ranking = VentanaRanking()
    ventana_juego = VentanaJuego()
    ventana_postnivel = VentanaPostnivel()

    # Instanciación
    froggie = Froggie()
    logica_inicio = LogicaInicio()
    logica_ranking = LogicaRanking()
    logica_juego = LogicaJuego(froggie)

    ventana_inicio.senal_enviar_usuario.connect(
        logica_inicio.revisar_nombre
    )
    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion
    )
    ventana_inicio.senal_abrir_juego.connect(
        ventana_juego.mostrar
    )
    ventana_inicio.senal_abrir_ranking.connect(
        logica_ranking.mostrar_ventana
    )
    logica_ranking.senal_mostrar.connect(
        ventana_ranking.mostrar
    )
    logica_ranking.senal_puntajes.connect(
        ventana_ranking.mostrar_puntajes
    )
    ventana_ranking.senal_abrir_inicio.connect(
        ventana_inicio.mostrar
    )
    logica_inicio.senal_enviar_nombre.connect(
        logica_ranking.guardar_nombre
    )
    ventana_juego.senal_iniciar_juego.connect(
         logica_juego.iniciar_juego
    )
    ventana_juego.senal_tecla.connect(
        logica_juego.froggie.avanzar
    )
    logica_juego.senal_chocar_caer.connect(
        ventana_juego.chocar_caer
    )
    logica_juego.froggie.senal_mover_rana.connect(
        ventana_juego.mover_rana
    )
    ventana_juego.senal_saltar.connect(
        logica_juego.froggie.saltar
    )
    logica_juego.senal_arriba_tronco.connect(
        ventana_juego.mover_rana
    )
    logica_juego.senal_aparecer_objeto.connect(
        ventana_juego.crear_objeto
    )
    logica_juego.senal_aparecer_auto.connect(
        ventana_juego.crear_auto
    )
    logica_juego.senal_aparecer_tronco.connect(
        ventana_juego.crear_tronco
    )
    logica_juego.senal_actualizar_labels.connect(
        ventana_juego.actualizar_labels
    )
    logica_juego.senal_agarrar_objeto.connect(
        ventana_juego.agarrar_objeto
    )
    ventana_juego.senal_parar.connect(
        logica_juego.parar
    )
    ventana_juego.senal_seguir.connect(
        logica_juego.iniciar_juego
    )
    ventana_juego.senal_salir.connect(
        logica_juego.cerrar
    )
    ventana_juego.senal_vidas_trampa.connect(
        logica_juego.froggie.vidas_trampa
    )
    logica_juego.senal_modificar_velocidad.connect(
        ventana_juego.cambiar_velocidades
    )
    logica_juego.froggie.senal_pasar_nivel.connect(
        ventana_postnivel.mostrar
    )
    logica_juego.froggie.senal_pasar_nivel.connect(
        ventana_juego.pasar_nivel
    )
    logica_juego.froggie.senal_pasar_nivel.connect(
        ventana_postnivel.cambiar_label
    )
    logica_juego.froggie.senal_pasar_nivel.connect(
        logica_juego.enviar_datos_partida
    )
    logica_juego.froggie.senal_pasar_nivel.connect(
        ventana_postnivel.mostrar
    )
    logica_juego.senal_datos_partida.connect(
        ventana_postnivel.mostrar_resumen
    )
    ventana_postnivel.senal_enviar_puntaje.connect(
        logica_ranking.agregar_puntaje
    )
    ventana_postnivel.senal_abrir_inicio.connect(
        logica_juego.cerrar
    )
    ventana_postnivel.senal_siguiente_nivel.connect(
        logica_juego.cambio_nivel
    )
    ventana_postnivel.senal_siguiente_nivel.connect(
        ventana_juego.mostrar
    )
    logica_juego.froggie.senal_actualizar_labels.connect(
        ventana_juego.actualizar_labels
    )
    ventana_juego.senal_pasar_nivel.connect(
        logica_juego.enviar_datos_partida
    )
    ventana_juego.senal_pasar_nivel.connect(
        ventana_juego.pasar_nivel
    )
    ventana_juego.senal_pasar_nivel.connect(
        ventana_postnivel.cambiar_label
    )
    ventana_juego.senal_pasar_nivel.connect(
        ventana_postnivel.mostrar
    )
    
    ventana_inicio.mostrar()
    app.exec()
