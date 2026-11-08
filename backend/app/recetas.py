"""Catálogo local de recetas para aprovechar los alimentos del inventario."""

RECETAS = [
    (
        1, "Batido de banano y fresa", [1, 8], 10, 2,
        "Pela el banano y córtalo en rodajas. Lava las fresas, retira el tallo y córtalas por la mitad. "
        "Coloca todo en la licuadora con un vaso de leche fría o agua. "
        "Licúa a velocidad alta por un minuto hasta obtener una mezcla homogénea y sin grumos. "
        "Prueba el dulzor y agrega miel si lo deseas. Sirve de inmediato con hielo.",
    ),
    (
        2, "Ensalada tropical", [2, 3, 8, 9], 15, 2,
        "Pela y corta la manzana en cubos medianos, sin corazón. "
        "Pela la naranja y separa los gajos quitando la membrana blanca. "
        "Lava las fresas, retira el tallo y córtalas por la mitad. "
        "Lava las uvas y córtalas por la mitad para que suelten el jugo. "
        "Mezcla todas las frutas en un bowl. "
        "Exprime el limón por encima y mezcla suavemente para bañar todo. Sirve bien fría.",
    ),
    (
        3, "Avena de manzana y canela", [2], 15, 2,
        "Pela la manzana, retira el corazón y córtala en cubos pequeños. "
        "En una olla a fuego medio, cocina la manzana con media taza de agua por 5 minutos removiendo ocasionalmente. "
        "Agrega una taza de avena en hojuelas y una taza más de leche o agua. "
        "Revuelve constantemente a fuego bajo por 7 minutos hasta que la avena espese. "
        "Agrega canela en polvo al gusto y una pizca de sal. "
        "Sirve caliente con miel por encima si lo deseas.",
    ),
    (
        4, "Jugo de naranja y mandarina", [3, 4, 13], 10, 3,
        "Lava bien las naranjas y mandarinas con agua fría. "
        "Parte los cítricos por la mitad con un cuchillo. "
        "Exprime cada mitad en un exprimidor manual hasta sacar todo el jugo. "
        "Cuela el jugo resultante para retirar semillas y fibra gruesa. "
        "Exprime el limón y agrega su jugo a la mezcla. "
        "Ajusta con agua fría y endulza a tu gusto. Sirve con hielo.",
    ),
    (
        5, "Ensalada de papaya y limón", [5, 13], 10, 2,
        "Lava la papaya por fuera con agua fría. "
        "Córtala por la mitad a lo largo y retira todas las semillas con una cuchara. "
        "Pela cada mitad con un cuchillo o pelador y córtala en cubos medianos. "
        "Coloca los cubos en un bowl. "
        "Exprime el limón generosamente por encima y agrega una pizca de sal si lo deseas. "
        "Mezcla suavemente. Refrigera 10 minutos antes de servir para potenciar el sabor.",
    ),
    (
        6, "Salsa de piña y mango", [6, 7, 13], 20, 4,
        "Pela la piña, retira el corazón duro y córtala en cubos de 1 cm. "
        "Pela el mango cortando los lados alrededor del hueso y luego en cubos pequeños. "
        "En una sartén a fuego medio-alto, cocina la piña y el mango por 5 minutos revolviendo frecuentemente. "
        "Exprime el limón sobre la mezcla y agrega una pizca de sal. "
        "Cocina 3 minutos más hasta que la fruta suelte su jugo y espese ligeramente. "
        "Retira del fuego y deja enfriar a temperatura ambiente. "
        "Sirve como acompañamiento de pollo, cerdo o como dip.",
    ),
    (
        7, "Parfait de mango y yogur", [7, 8, 9], 10, 2,
        "Pela el mango, córtalo en cubos pequeños desechando el hueso. "
        "Lava las fresas, retira el tallo y córtalas en láminas finas. "
        "Lava las uvas y córtalas por la mitad. "
        "En vasos altos o tazones, coloca una capa generosa de yogur como base. "
        "Agrega una capa de mango, luego de fresa y por último de uva. "
        "Repite las capas hasta llenar el vaso terminando con frutas. "
        "Refrigera por 15 minutos antes de servir. Puedes añadir granola encima para más textura.",
    ),
    (
        8, "Limonada de maracuyá", [12, 13], 10, 4,
        "Parte los maracuyás por la mitad con un cuchillo. "
        "Extrae la pulpa completa con una cuchara y colócala en una jarra. "
        "Exprime los limones y agrega su jugo a la jarra. "
        "Vierte agua fría al gusto, entre 3 y 4 tazas según la intensidad que prefieras. "
        "Agrega azúcar o miel y revuelve vigorosamente hasta disolver. "
        "Prueba y ajusta el dulzor. Sirve con abundante hielo y una rodaja de limón.",
    ),
    (
        9, "Ensalada de pera y uva", [9, 10, 20], 15, 2,
        "Lava y seca bien las hojas de lechuga, luego córtalas o desgárrralas en trozos medianos. "
        "Pela la pera, retira el corazón y córtala en láminas finas. "
        "Lava las uvas y córtalas por la mitad. "
        "Coloca la lechuga como base en un plato o bowl. "
        "Distribuye la pera y las uvas por encima. "
        "Prepara una vinagreta mezclando aceite, vinagre, sal y pimienta en un tazón pequeño. "
        "Vierte la vinagreta sobre la ensalada justo antes de servir.",
    ),
    (
        10, "Guacamole fresco", [11, 14, 18, 13, 30], 15, 4,
        "Corta los aguacates por la mitad a lo largo, retira el hueso con cuidado y extrae la pulpa con una cuchara. "
        "En un bowl, aplasta la pulpa con un tenedor hasta obtener una textura cremosa con algunos trozos pequeños. "
        "Corta el tomate en cubos pequeños, retirando las semillas para evitar exceso de líquido. "
        "Pica la cebolla y el cilantro muy finamente. "
        "Incorpora el tomate, la cebolla y el cilantro al aguacate. "
        "Exprime el limón, agrega sal y pimienta al gusto y mezcla bien. "
        "Prueba y ajusta la sazón. Sirve de inmediato o cubre con plástico pegado a la superficie para evitar que se oxide.",
    ),
    (
        11, "Ensalada de aguacate y pepino", [11, 15, 18, 13], 15, 2,
        "Pela el pepino y córtalo en medias lunas de medio centímetro de grosor. "
        "Corta el aguacate por la mitad, retira el hueso y córtalo en cubos medianos. "
        "Pica la cebolla en juliana muy delgada. "
        "Coloca el pepino y la cebolla en un bowl y mezcla. "
        "Incorpora el aguacate con cuidado para no deshacerlo. "
        "Exprime el limón generosamente por encima. "
        "Agrega sal al gusto, mezcla con suavidad y sirve de inmediato.",
    ),
    (
        12, "Pico de gallo", [14, 18, 30, 13], 15, 4,
        "Lava bien los tomates y córtalos en cubos pequeños retirando el centro con semillas. "
        "Pica la cebolla en brunoise muy fino para que no sea muy intensa. "
        "Lava el cilantro, sécalo y pícalo finamente usando solo las hojas y los tallos tiernos. "
        "Mezcla el tomate, la cebolla y el cilantro en un bowl. "
        "Exprime el limón sobre la mezcla y agrega sal al gusto. "
        "Revuelve bien y deja reposar 10 minutos para que se integren los sabores. "
        "Sirve como acompañamiento o con tortillas de maíz.",
    ),
    (
        13, "Gazpacho de tomate", [14, 15, 18, 13], 20, 4,
        "Lava los tomates y córtalos en cuartos. "
        "Pela el pepino, retira las semillas con una cuchara y córtalo en trozos. "
        "Pela y trocea la cebolla en trozos grandes. "
        "Coloca tomate, pepino y cebolla en la licuadora. "
        "Agrega el jugo del limón, una pizca de sal y un chorrito de aceite de oliva. "
        "Licúa a velocidad alta por 2 minutos hasta conseguir una mezcla completamente fina. "
        "Cuela si deseas una textura más suave. "
        "Refrigera por al menos 1 hora antes de servir. Sirve muy frío con unas gotas de aceite de oliva.",
    ),
    (
        14, "Salteado de pimentón y zanahoria", [16, 17, 18], 20, 3,
        "Pela la zanahoria y córtala en bastones delgados o en rodajas diagonales. "
        "Corta el pimentón retirando el tallo y las semillas, luego en tiras de 1 cm. "
        "Pica la cebolla en juliana. "
        "Calienta una sartén amplia o wok con un poco de aceite a fuego alto. "
        "Saltea la zanahoria primero por 3 minutos ya que tarda más en cocinarse. "
        "Agrega el pimentón y la cebolla y cocina revolviendo constantemente por 5 minutos. "
        "Sazona con sal, pimienta y unas gotas de limón. Sirve caliente como acompañamiento.",
    ),
    (
        15, "Ensalada crocante", [15, 17, 20, 24], 15, 3,
        "Lava y seca la lechuga, luego córtala en trozos medianos con las manos. "
        "Pela el pepino y córtalo en medias lunas finas. "
        "Pela la zanahoria y rállala con el lado grueso del rallador. "
        "Corta el repollo en tiras muy finas desechando el tronco duro. "
        "Mezcla todos los vegetales en un bowl grande. "
        "Para el aderezo, mezcla aceite, jugo de limón, sal y pimienta en un tazón pequeño. "
        "Vierte el aderezo sobre la ensalada justo antes de servir para conservar la textura crocante.",
    ),
    (
        16, "Crema de brócoli", [22, 18, 17, 21], 30, 4,
        "Separa el brócoli en floretes medianos y la coliflor en trozos similares. "
        "Pela la zanahoria y córtala en rodajas. Pica la cebolla en trozos medianos. "
        "En una olla grande, calienta aceite a fuego medio y sofríe la cebolla por 3 minutos hasta que esté transparente. "
        "Agrega la zanahoria, el brócoli y la coliflor a la olla. "
        "Cubre con 4 tazas de agua o caldo de verduras con sal. "
        "Cocina a fuego medio tapado por 20 minutos hasta que todos los vegetales estén muy suaves. "
        "Licúa todo con una licuadora de inmersión o transfiere a la licuadora por tandas. "
        "Regresa a la olla, ajusta la sal y calienta a fuego bajo. Sirve caliente.",
    ),
    (
        17, "Habichuelas con tomate", [23, 14, 18], 25, 3,
        "Lava las habichuelas y retira los extremos y los hilos de los lados con los dedos. "
        "Córtalas en trozos de 4 cm aproximadamente. "
        "Cocínalas en agua hirviente con sal por 10 minutos hasta que estén tiernas pero aún firmes. Escurre y reserva. "
        "Pica el tomate en cubos medianos y la cebolla en brunoise fino. "
        "En una sartén con aceite, sofríe la cebolla a fuego medio por 3 minutos hasta dorar. "
        "Agrega el tomate y cocina el guiso por 7 minutos revolviendo hasta que espese. "
        "Incorpora las habichuelas al guiso, mezcla y cocina 2 minutos más. Sazona con sal y sirve caliente.",
    ),
    (
        18, "Repollo salteado", [24, 18, 16, 19], 20, 3,
        "Corta el repollo en cuartos, retira el tronco central duro y luego córtalo en tiras delgadas. "
        "Pica la cebolla en juliana y el pimentón en tiras finas. "
        "Calienta una sartén grande con aceite a fuego alto. "
        "Sofríe la cebolla por 2 minutos removiendo constantemente. "
        "Agrega el pimentón y cocina 2 minutos más. "
        "Incorpora el repollo y saltea revolviendo frecuentemente por 7 a 8 minutos. "
        "El repollo debe quedar tierno pero no aguado. "
        "Sazona con sal y pimienta al gusto. Sirve caliente como acompañamiento.",
    ),
    (
        19, "Patacones con hogao", [25, 14, 18, 30], 35, 4,
        "Pela el plátano verde y córtalo en rodajas gruesas de unos 3 cm. "
        "Calienta abundante aceite en una sartén a fuego medio-alto y fríe las rodajas por 3 minutos por cada lado hasta dorar. "
        "Retira las rodajas y aplástalas individualmente con el fondo de un vaso o plato hasta dejarlas de 1 cm de grosor. "
        "Regresa al aceite caliente y fríe 2 minutos más por cada lado hasta que estén bien dorados y crujientes. "
        "Escurre sobre papel absorbente y sazona con sal inmediatamente. "
        "Para el hogao, sofríe la cebolla picada en aceite por 3 minutos, agrega el tomate en cubos y cocina a fuego medio por 10 minutos hasta obtener una salsa espesa. "
        "Agrega el cilantro picado y mezcla. Sirve los patacones calientes cubiertos con el hogao.",
    ),
    (
        20, "Papas criollas al cilantro", [26, 30, 18], 30, 4,
        "Lava muy bien las papas criollas restregando la piel bajo agua corriente. "
        "Cocínalas enteras con cáscara en agua con sal a fuego medio por 15 a 18 minutos, hasta que al pincharlas con un tenedor entren fácilmente. "
        "Escurre y deja enfriar ligeramente, luego parte las más grandes por la mitad. "
        "Pica la cebolla finamente y el cilantro en trozos medianos. "
        "En una sartén con aceite, sofríe la cebolla a fuego medio por 3 minutos hasta que esté dorada. "
        "Agrega las papas y saltéalas revolviendo con cuidado por 5 minutos. "
        "Incorpora el cilantro, mezcla y retira del fuego. Sirve caliente.",
    ),
    (
        21, "Yuca con guacamole", [27, 11, 14, 13], 35, 4,
        "Pela la yuca con un cuchillo grande y córtala en trozos de 5 cm. "
        "Retira el hilo central de cada trozo si está presente. "
        "Hierve en agua abundante con sal a fuego alto por 25 a 30 minutos hasta que esté muy tierna. "
        "Mientras tanto, prepara el guacamole: corta el aguacate, extrae la pulpa y aplástala con un tenedor. "
        "Corta el tomate en cubos pequeños sin semillas y mézclalo con el aguacate. "
        "Exprime el limón sobre la mezcla, agrega sal y mezcla bien. "
        "Escurre la yuca cocida y sirve caliente acompañada con el guacamole fresco al lado.",
    ),
    (
        22, "Sopa de arracacha", [28, 17, 18, 30], 40, 4,
        "Pela la arracacha y la zanahoria, y córtalas en trozos medianos. "
        "Pica la cebolla en trozos grandes. "
        "En una olla a fuego medio, calienta aceite y sofríe la cebolla por 3 minutos hasta que esté transparente. "
        "Agrega la arracacha y la zanahoria a la olla. "
        "Cubre con 5 tazas de agua o caldo de verduras y agrega sal. "
        "Cocina tapado a fuego medio por 25 minutos hasta que los tubérculos estén muy suaves. "
        "Licúa todo directamente en la olla con una licuadora de inmersión hasta obtener una crema homogénea. "
        "Ajusta la sal y la consistencia agregando agua si queda muy espesa. "
        "Sirve caliente con cilantro picado por encima.",
    ),
    (
        23, "Ensalada de remolacha", [29, 17, 20, 13], 30, 3,
        "Lava bien las remolachas frotando la piel con un cepillo. "
        "Cocínalas enteras con cáscara en agua hirviente por 25 a 30 minutos hasta que al pincharlas con un tenedor entren sin resistencia. "
        "Deja enfriar completamente, luego pela con los dedos y la cáscara saldrá fácilmente. "
        "Córtala en cubos medianos. "
        "Pela la zanahoria y rállala con el lado grueso del rallador. "
        "Lava y seca la lechuga y córtala en trozos. "
        "Mezcla la remolacha y la zanahoria en un bowl, exprime el limón y agrega sal al gusto. "
        "Sirve sobre las hojas de lechuga.",
    ),
    (
        24, "Sancocho de verduras", [26, 27, 28, 17, 18, 30], 50, 6,
        "Pela y corta en trozos grandes la papa criolla, la yuca y la arracacha. "
        "Pela la zanahoria y córtala en rodajas gruesas. "
        "Pica la cebolla en trozos medianos. "
        "En una olla grande, calienta aceite y sofríe la cebolla por 3 minutos. "
        "Agrega todos los tubérculos y la zanahoria a la olla. "
        "Cubre con abundante agua caliente, unas 8 tazas, y agrega sal generosamente. "
        "Cocina a fuego medio-alto por 30 a 35 minutos hasta que todo esté muy tierno. "
        "Verifica la sazón e incorpora el cilantro picado en los últimos 2 minutos. "
        "Sirve caliente en platos hondos con el caldo abundante.",
    ),
    (
        25, "Sopa de verduras verdes", [15, 22, 23, 20], 30, 4,
        "Lava bien el pepino, el brócoli, las habichuelas y la lechuga. "
        "Corta el pepino en trozos, separa el brócoli en floretes y corta las habichuelas en trozos de 3 cm. "
        "En una olla con aceite a fuego medio, saltea brevemente todas las verduras por 2 minutos. "
        "Cubre con 4 tazas de agua o caldo de verduras con sal y tapa la olla. "
        "Cocina a fuego medio por 15 minutos hasta que todo esté bien tierno. "
        "Agrega la lechuga y cocina 2 minutos más. "
        "Licúa todo hasta obtener una sopa cremosa y homogénea. "
        "Regresa a la olla, ajusta la sal y calienta a fuego bajo sin dejar hervir. Sirve con un hilo de aceite de oliva.",
    ),
    (
        26, "Bowl de frutas con maracuyá", [1, 5, 7, 12, 13], 15, 2,
        "Pela el banano y córtalo en rodajas. "
        "Pela la papaya, retira las semillas y córtala en cubos medianos. "
        "Pela el mango cortando los lados y luego en cubos. "
        "Parte el maracuyá por la mitad y extrae la pulpa con una cuchara. "
        "Exprime el limón y mezcla su jugo con la pulpa de maracuyá. "
        "Acomoda el banano, la papaya y el mango en un bowl. "
        "Vierte la mezcla de maracuyá y limón por encima cubriendo todas las frutas. "
        "Refrigera 10 minutos y sirve frío.",
    ),
    (
        27, "Ensalada de repollo y manzana", [2, 20, 24, 13], 15, 3,
        "Corta el repollo en cuartos, retira el tronco duro y córtalo en tiras muy finas. "
        "Pela la manzana, retira el corazón y córtala en juliana delgada. "
        "Para evitar que la manzana oxide, rocía unas gotas de limón inmediatamente. "
        "Lava y seca las hojas de lechuga. "
        "Mezcla el repollo y la manzana en un bowl. "
        "Exprime el resto del limón por encima, agrega sal al gusto y mezcla bien. "
        "Sirve sobre las hojas de lechuga como base.",
    ),
    (
        28, "Pimentones rellenos de verduras", [16, 17, 22, 18], 40, 4,
        "Precalienta el horno a 190 grados. "
        "Corta la parte superior de cada pimentón a modo de tapa y retira todas las semillas con cuidado. "
        "Pica la zanahoria, el brócoli y la cebolla en trozos muy pequeños. "
        "En una sartén con aceite a fuego medio, sofríe la cebolla por 2 minutos. "
        "Agrega la zanahoria y el brócoli y cocina 5 minutos revolviendo hasta que estén tiernos. "
        "Sazona con sal y pimienta. "
        "Rellena cada pimentón con la mezcla de verduras presionando suavemente para compactar. "
        "Coloca en una bandeja resistente al horno y hornea por 20 minutos hasta que el pimentón esté tierno. Sirve caliente.",
    ),
    (
        29, "Tostadas de aguacate y tomate", [11, 14, 13, 30], 15, 2,
        "Tuesta las rebanadas de pan hasta que estén doradas y crujientes. "
        "Corta el aguacate por la mitad, retira el hueso y extrae la pulpa con una cuchara. "
        "En un bowl pequeño, aplasta el aguacate con un tenedor. "
        "Agrega el jugo del limón y sal al gusto, mezcla hasta obtener una pasta cremosa. "
        "Corta el tomate en rodajas finas o en cubos pequeños. "
        "Extiende generosamente el aguacate sobre cada tostada. "
        "Coloca el tomate encima y termina con cilantro fresco picado. Sirve de inmediato.",
    ),
    (
        30, "Salpicón de frutas", [1, 3, 4, 6, 7, 13], 20, 6,
        "Pela el banano y córtalo en rodajas. "
        "Pela la naranja y la mandarina, separa los gajos y retira la membrana blanca. "
        "Pela la piña, retira el corazón duro y córtala en cubos pequeños. "
        "Pela el mango, separa la pulpa del hueso y córtala en cubos. "
        "Mezcla todas las frutas en un bowl grande con cuidado para no aplastarlas. "
        "Exprime el limón y vierte su jugo por encima de todas las frutas. "
        "Revuelve suavemente para distribuir el jugo. "
        "Refrigera por al menos 30 minutos para que se integren los sabores. Sirve muy frío.",
    ),
]


def obtener_catalogo():
    return [
        {
            "id_receta": rid,
            "titulo": titulo,
            "ingredientes": ingredientes,
            "minutos_prep": minutos,
            "porciones": porciones,
            "pasos": pasos,
        }
        for rid, titulo, ingredientes, minutos, porciones, pasos in RECETAS
    ]
