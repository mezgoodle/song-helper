import tekore as tk
import os

from unittest import TestCase

from .utils import SpotifyUtils


class TestSpotifyUtils(TestCase):
    def setUp(self) -> None:
        self.util_obj = SpotifyUtils()
        self.util_obj_1 = SpotifyUtils(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('REDIRECT_URI'))

    def test_creation(self):
        """Our object must be an instance of SpotifyUtils class"""
        self.assertIsInstance(self.util_obj, SpotifyUtils)
        self.assertIsInstance(self.util_obj_1, SpotifyUtils)

    def test_default_fields(self):
        """If we do not set params in constructor, they must be set as default. And test their types"""
        self.assertIsNotNone(self.util_obj.spt)
        self.assertIsInstance(self.util_obj.spt, tk.Spotify)
        self.assertIsNotNone(self.util_obj.redirect_uri)
        self.assertIsInstance(self.util_obj.redirect_uri, str)
        self.assertIsNotNone(self.util_obj.client_secret)
        self.assertIsInstance(self.util_obj.client_secret, str)
        self.assertIsNotNone(self.util_obj.client_id)
        self.assertIsInstance(self.util_obj.client_id, str)

    def test_custom_fields(self):
        """If we set params in constructor, they must not be set as default. And test their types and values"""
        self.assertIsNotNone(self.util_obj_1.spt)
        self.assertIsInstance(self.util_obj_1.spt, tk.Spotify)
        self.assertIsNotNone(self.util_obj_1.redirect_uri)
        self.assertIsInstance(self.util_obj_1.redirect_uri, str)
        self.assertEqual(self.util_obj_1.redirect_uri, os.getenv('REDIRECT_URI'))
        self.assertIsNotNone(self.util_obj_1.client_secret)
        self.assertIsInstance(self.util_obj_1.client_secret, str)
        self.assertEqual(self.util_obj_1.client_secret, os.getenv('CLIENT_SECRET'))
        self.assertIsNotNone(self.util_obj_1.client_id)
        self.assertIsInstance(self.util_obj_1.client_id, str)
        self.assertEqual(self.util_obj_1.client_id, os.getenv('CLIENT_ID'))

    def test_get_song_features_method(self):
        """Test getting features from the song"""
        song_features = self.util_obj.get_song_features('4iLqG9SeJSnt0cSPICSjxv')
        song_features_1 = self.util_obj_1.get_song_features('4iLqG9SeJSnt0cSPICSjxv')
        self.assertIsNotNone(song_features)
        self.assertIsNotNone(song_features_1)
        self.assertEqual(len(song_features), 11)
        self.assertIsInstance(song_features, dict)
        self.assertIsInstance(song_features_1, dict)
        self.assertIsNotNone(song_features['acousticness'])
        self.assertIsNotNone(song_features_1['speechiness'])
        self.assertIsInstance(song_features['key'], int)

    def get_song_meta(self):
        """Test getting meta info from the song"""
        song_info = self.util_obj.get_song_meta('4iLqG9SeJSnt0cSPICSjxv')
        song_info_1 = self.util_obj_1.get_song_meta('4iLqG9SeJSnt0cSPICSjxv')
        self.assertIsNotNone(song_info)
        self.assertIsNotNone(song_info_1)
        self.assertEqual(len(song_info), 7)
        self.assertIsInstance(song_info, dict)
        self.assertIsInstance(song_info_1, dict)
        self.assertIsNotNone(song_info['name'])
        self.assertIsNotNone(song_info_1['album'])
        self.assertIsInstance(song_info['id'], str)

    def test_get_albums_id(self):
        self.skipTest('Not ready')

    def test_get_album_songs_id(self):
        self.skipTest('Not ready')

    def test_get_song_analise(self):
        self.skipTest('Not ready')

    def test_get_song(self):
        self.skipTest('Not ready')

    def test_download_albums(self):
        self.skipTest('Not ready')

    def test_download_playlist(self):
        self.skipTest('Not ready')

    def tearDown(self) -> None:
        del self.util_obj
        del self.util_obj_1
