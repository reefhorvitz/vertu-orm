from graphene import Node


class RegularIdNode(Node):
    class Meta:
        name = 'regular_id_node'

    @classmethod
    def to_global_id(cls, type, id):
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        model = only_type._meta.model
        return model.objects.get(id=global_id)
