# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MikroAct'
        db.create_table(u'acts_mikroact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('shortcuts.DefaultCharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('location_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('location_address', self.gf('shortcuts.DefaultCharField')(max_length=255, blank=True)),
            ('status', self.gf(u'dj.choices.fields.ChoiceField')(unique=False, primary_key=False, db_column=None, blank=False, default=1, null=False, _in_south=True, db_index=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'acts', ['MikroAct'])

        # Adding model 'CollectionMembership'
        db.create_table(u'acts_collectionmembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mikro_act', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acts.MikroAct'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acts.Collection'])),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'acts', ['CollectionMembership'])

        # Adding unique constraint on 'CollectionMembership', fields ['mikro_act', 'collection']
        db.create_unique(u'acts_collectionmembership', ['mikro_act_id', 'collection_id'])

        # Adding model 'CollectionFollow'
        db.create_table(u'acts_collectionfollow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['acts.Collection'])),
            ('date_followed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'acts', ['CollectionFollow'])

        # Adding unique constraint on 'CollectionFollow', fields ['user', 'collection']
        db.create_unique(u'acts_collectionfollow', ['user_id', 'collection_id'])

        # Adding model 'Collection'
        db.create_table(u'acts_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('shortcuts.DefaultCharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'acts', ['Collection'])


    def backwards(self, orm):
        # Removing unique constraint on 'CollectionFollow', fields ['user', 'collection']
        db.delete_unique(u'acts_collectionfollow', ['user_id', 'collection_id'])

        # Removing unique constraint on 'CollectionMembership', fields ['mikro_act', 'collection']
        db.delete_unique(u'acts_collectionmembership', ['mikro_act_id', 'collection_id'])

        # Deleting model 'MikroAct'
        db.delete_table(u'acts_mikroact')

        # Deleting model 'CollectionMembership'
        db.delete_table(u'acts_collectionmembership')

        # Deleting model 'CollectionFollow'
        db.delete_table(u'acts_collectionfollow')

        # Deleting model 'Collection'
        db.delete_table(u'acts_collection')


    models = {
        u'acts.collection': {
            'Meta': {'object_name': 'Collection'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'following'", 'symmetrical': 'False', 'through': u"orm['acts.CollectionFollow']", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mikro_acts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['acts.MikroAct']", 'through': u"orm['acts.CollectionMembership']", 'symmetrical': 'False'}),
            'name': ('shortcuts.DefaultCharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'acts.collectionfollow': {
            'Meta': {'unique_together': "(('user', 'collection'),)", 'object_name': 'CollectionFollow'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acts.Collection']"}),
            'date_followed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'acts.collectionmembership': {
            'Meta': {'unique_together': "(('mikro_act', 'collection'),)", 'object_name': 'CollectionMembership'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acts.Collection']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mikro_act': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acts.MikroAct']"})
        },
        u'acts.mikroact': {
            'Meta': {'object_name': 'MikroAct'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_address': ('shortcuts.DefaultCharField', [], {'max_length': '255', 'blank': 'True'}),
            'location_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'status': (u'dj.choices.fields.ChoiceField', [], {'unique': 'False', 'primary_key': 'False', 'db_column': 'None', 'blank': 'False', u'default': '1', 'null': 'False', '_in_south': 'True', 'db_index': 'False'}),
            'title': ('shortcuts.DefaultCharField', [], {'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['acts']