from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask

class WeatherService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def get_weather(ctx, city, zip_code):
        xml = f"""
        <weather>
            <location>{city or zip_code}</location>
            <temperature>32°C</temperature>
            <humidity>60%</humidity>
            <condition>Sunny</condition>
        </weather>
        """
        return xml

soap_app = Application([WeatherService], 'weather.soap',
                       in_protocol=Soap11(), out_protocol=Soap11())
wsgi_app = WsgiApplication(soap_app)