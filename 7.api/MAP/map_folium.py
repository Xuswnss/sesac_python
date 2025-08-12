from flask import Flask, request, render_template
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map_view():
    latitude, longitude = 37.5193, 126.9408
    if request.method == 'POST':
        latitude = float(request.form.get('latitude', latitude))
        longitude = float(request.form.get('longitude', longitude))
        
    map_63_building = folium.Map(location=[latitude, longitude], zoom_start=15)    
    folium.Marker([latitude, longitude], popup='6.3 Building').add_to(map_63_building)
    map_html = map_63_building

    return render_template('map.html', latitude=latitude, longitude=longitude, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)

