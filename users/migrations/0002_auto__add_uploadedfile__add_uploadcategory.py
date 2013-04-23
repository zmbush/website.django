# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedFile'
        db.create_table(u'users_uploadedfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UploadCategory'])),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('release_notes', self.gf('django.db.models.fields.TextField')()),
            ('major_version', self.gf('django.db.models.fields.IntegerField')()),
            ('minor_version', self.gf('django.db.models.fields.IntegerField')()),
            ('version_letter', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['UploadedFile'])

        # Adding model 'UploadCategory'
        db.create_table(u'users_uploadcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['UploadCategory'])


    def backwards(self, orm):
        # Deleting model 'UploadedFile'
        db.delete_table(u'users_uploadedfile')

        # Deleting model 'UploadCategory'
        db.delete_table(u'users_uploadcategory')


    models = {
        u'users.uploadcategory': {
            'Meta': {'object_name': 'UploadCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UploadCategory']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_version': ('django.db.models.fields.IntegerField', [], {}),
            'minor_version': ('django.db.models.fields.IntegerField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'release_notes': ('django.db.models.fields.TextField', [], {}),
            'version_letter': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['users']