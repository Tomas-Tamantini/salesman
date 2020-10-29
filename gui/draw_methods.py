from .canvas import canvas, canvas_width, canvas_height

city_radius = 10
highlight_color = '#f5dd29'
highlight_color = '#00a5ff'


def draw_city(position, city_name, highlight=False):
    xc, yc = position
    x0 = xc - city_radius
    x1 = xc + city_radius
    y0 = yc - city_radius
    y1 = yc + city_radius
    color = highlight_color if highlight else '#00a5ff'
    canvas.create_oval(x0, y0, x1, y1, fill='#ffae19', outline=color, width=2)
    canvas.create_text(xc, yc, text=city_name[:2], fill='#0a1172')


def draw_road(pos_a, pos_b):
    canvas.create_line(*pos_a, *pos_b, width=2, fill=highlight_color)


def draw_region(region, route=None):
    canvas.delete('all')
    padding = city_radius + 0.1 * canvas_width
    min_x, min_y, max_x, max_y = region.dimensions.values()
    region_width = max(max_x - min_x, 2 * city_radius)
    region_height = max(max_y - min_y, 2 * city_radius)

    scaling_factor_x = (canvas_width - 2 * padding) / region_width
    scaling_factor_y = (canvas_height - 2 * padding) / region_height
    scaling_factor = min(scaling_factor_x, scaling_factor_y)
    off_x = min_x - padding / scaling_factor
    off_y = max_y + padding / scaling_factor

    def coordinate_transformer(pos):
        return (pos.x - off_x) * scaling_factor, -(pos.y - off_y) * scaling_factor

    if route is not None:
        for i in range(len(route)):
            city = route[i]
            previous_city = route[i - 1]
            pos_a = coordinate_transformer(city.position)
            pos_b = coordinate_transformer(previous_city.position)
            draw_road(pos_a, pos_b)
    for city in region.cities:
        position = coordinate_transformer(city.position)
        highlight = route is not None and city in route
        draw_city(position, city.name, highlight)
