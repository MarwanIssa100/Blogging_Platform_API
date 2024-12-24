from rest_framework import serializers
from .models import Blog , Category , Tag

class TagSerializer(serializers.ListField):
    class Meta:
        model = Tag
        fields = ['name']
        
    def create(self, validated_data):
        instance = self.Meta.model
        tag = instance.objects.create(**validated_data)
        return tag
    
    def to_representation(self, data):
        return data.values_list('name', flat=True)
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category    

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False)
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Author' , 'Category','tags']
        
        
        
    def create(self, validated_data):
        tag_names = validated_data.pop('tags',[])if "tags" in validated_data else []


        blog = self.Meta.model.objects.create(**validated_data)
        
        if tag_names:
            tags = []
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name)
                tags.append(tag)
                
            blog.tags.set(tags)
        

        return blog
    
    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tags', []) if "tags" in validated_data else []


        blog = super().update(instance, validated_data)
        
        if tag_names:
            tags = []
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name)
                tags.append(tag)
                
            blog.tags.set(tags)
        
            
        return blog
    
    def to_representation(self, instance):
        # Override to_representation to display tag names instead of IDs
        representation = super().to_representation(instance)
        representation['Category'] = CategorySerializer(instance.Category).data if instance.Category else None
        return representation
