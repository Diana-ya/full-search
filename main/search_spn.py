def find_spn(resp):
    top = resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    x, y = top['boundedBy']['Envelope']['lowerCorner'].split(' '), \
        top['boundedBy']['Envelope']['upperCorner'].split(' ')
    width = float(y[0]) - float(x[0])
    height = float(y[1]) - float(x[1])
    return str(width), str(height)
