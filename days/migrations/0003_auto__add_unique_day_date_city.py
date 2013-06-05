# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Day', fields ['date', 'city']
        db.create_unique(u'days_day', ['date', 'city_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Day', fields ['date', 'city']
        db.delete_unique(u'days_day', ['date', 'city_id'])


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
            'Meta': {'unique_together': "(('date', 'city'),)", 'object_name': 'Day'},
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