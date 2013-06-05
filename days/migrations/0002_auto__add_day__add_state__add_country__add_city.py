# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'days_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['days.City'])),
            ('temp', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'days', ['Day'])

        # Adding model 'State'
        db.create_table(u'days_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['days.Country'])),
        ))
        db.send_create_signal(u'days', ['State'])

        # Adding model 'Country'
        db.create_table(u'days_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'days', ['Country'])

        # Adding model 'City'
        db.create_table(u'days_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['days.State'])),
        ))
        db.send_create_signal(u'days', ['City'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'days_day')

        # Deleting model 'State'
        db.delete_table(u'days_state')

        # Deleting model 'Country'
        db.delete_table(u'days_country')

        # Deleting model 'City'
        db.delete_table(u'days_city')


    models = {
        u'days.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['days.State']"})
        },
        u'days.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'days.day': {
            'Meta': {'object_name': 'Day'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['days.City']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.IntegerField', [], {})
        },
        u'days.state': {
            'Meta': {'object_name': 'State'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['days.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['days']