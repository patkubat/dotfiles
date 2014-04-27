from time import time

class Py3status:
    """
    Simply output the currently logged in user in i3bar.

    Inspired by i3 FAQ:
        https://faq.i3wm.org/question/1618/add-user-name-to-status-bar/
    """
    def spotify(self, i3status_output_json, i3status_config):
        """
        We use the getpass module to get the current user.
        """
        import dbus
        bus = dbus.SessionBus()
        player = bus.get_object('com.spotify.qt', '/')
        iface = dbus.Interface(player, 'org.freedesktop.MediaPlayer2')
        info = iface.GetMetadata()
        # OUT: [dbus.String(u'xesam:album'), dbus.String(u'xesam:title'), dbus.String(u'xesam:trackNumber'), dbus.String(u'xesam:artist'), dbus.String(u'xesam:discNumber'), dbus.String(u'mpris:trackid'), dbus.String(u'mpris:length'), dbus.String(u'mpris:artUrl'), dbus.String(u'xesam:autoRating'), dbus.String(u'xesam:contentCreated'), dbus.String(u'xesam:url')]
        #spot += str(info['xesam:title']) 
        #spot += str(info['xesam:artist'][0]) 
        #spot += str(info['xesam:album'])
        # + " - " + str(info['xesam:title'])
        #response = 'test'
        spot = '{}'.format(str(info['xesam:title']) + ' - ' + str(info['xesam:artist'][0]) + ' - ' + str(info['xesam:album']))
        response = {'full_text': spot, 'name': 'spotify', 'instance': 'first'}
        response['cached_until'] = time()
        #response['color'] = i3status_config['color_good']
        response['color'] = "#80FF00"
        return (0, response)