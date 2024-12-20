from django import template

register = template.Library()

SUBCATEGORY_MAPPING = {
    'paletas_ojos': 'Paletas de ojos',
    'paletas_rostro': 'Paletas para rostro',
    'bases_maquillaje': 'Bases de maquillaje',
    'colorete': 'Coloretes',
    'bronceadores': 'Bronceadores y contouring',
    'correctores': 'Correctores',
    'iluminadores': 'Iluminadores',
    'fijadores': 'Fijadores',
    'polvos': 'Polvos',
    'prebases_rostro': 'Prebases de rostro',
    'mascaras': 'Máscaras de ojos',
    'sombras': 'Sombras de ojos',
    'lapices': 'Lápices de ojos',
    'cejas': 'Cejas',
    'delineadores': 'Delineadores',
    'prebases_ojos': 'Prebases para ojos',
    'labiales': 'Labiales',
    'brillos_labios': 'Brillos de labios',
    'lapices_contorno': 'Lápices de contorno',
    'prebases_labios': 'Prebases para labios',
    'esmaltes': 'Esmaltes de uñas',
    'cuidado_unas': 'Cuidado de las uñas',
    'manicura_francesa': 'Manicura francesa',
    'quitaesmaltes': 'Quitaesmaltes',
    'fijadores_esmalte': 'Fijadores de esmalte',
}

@register.filter(name='subcategory_label')
def subcategory_label(value):
    """Convierte la subcategoría a un formato legible"""
    return SUBCATEGORY_MAPPING.get(value, value)  # Si no encuentra, retorna el valor tal cual