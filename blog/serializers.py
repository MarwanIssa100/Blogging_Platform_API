from rest_framework import serializers
from .models import Blog , Tag , Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
        
    def create(self, validated_data):
        instance = self.Meta.model
        tag = instance.objects.create(**validated_data)
        return tag
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category    

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    Category = CategorySerializer(many=False,required=False)
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Author' , 'Category', 'tags']
        
        
        
    def create(self, validated_data):
        tags_names = validated_data.pop('tags', [])
        category_data = validated_data.pop('Category', None)
        
        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            validated_data['Category'] = category

        blog = self.Meta.model.objects.create(**validated_data)
            
        for tag_name in tags_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)  # Use or create tags
            blog.tags.add(tag)
            

        return blog
    
    def to_representation(self, instance):
        # Override to_representation to display tag names instead of IDs
        representation = super().to_representation(instance)
        representation['tags'] = TagSerializer(instance.tags.all(), many=True).data
        representation['Category'] = CategorySerializer(instance.Category).data if instance.Category else None
        return representation
