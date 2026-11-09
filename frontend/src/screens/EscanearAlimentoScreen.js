import { useCallback } from 'react';
import { View, StyleSheet, Platform } from 'react-native';
import { Text } from 'react-native-paper';
import { useFocusEffect } from '@react-navigation/native';
import { colores, fuentes, sombras } from '../theme/theme';

export default function EscanearAlimentoScreen() {
  useFocusEffect(
    useCallback(() => {
      if (Platform.OS === 'web') document.title = 'Identificar alimento · FreshTrack';
    }, [])
  );

  return (
    <View style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.emoji}>📱</Text>
        <Text style={styles.titulo}>Demo en vivo</Text>
        <Text style={styles.mensaje}>
          Esta función usa inteligencia artificial para identificar frutas y verduras con la cámara de tu celular.
        </Text>
        <Text style={styles.mensaje}>
          No está disponible en esta versión web de la demo.{'\n'}
          Pídele a los expositores que te la muestren en el celular. 🙌
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colores.fondo,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  card: {
    backgroundColor: colores.blanco,
    borderRadius: 24,
    padding: 28,
    alignItems: 'center',
    boxShadow: sombras.media,
    maxWidth: 420,
    width: '100%',
  },
  emoji: {
    fontSize: 64,
    marginBottom: 16,
  },
  titulo: {
    fontFamily: fuentes.titulo,
    fontSize: 26,
    color: colores.selva,
    marginBottom: 16,
    textAlign: 'center',
  },
  mensaje: {
    fontFamily: fuentes.textoMedio,
    fontSize: 15,
    color: colores.tinta,
    textAlign: 'center',
    lineHeight: 22,
    marginBottom: 12,
  },
});
