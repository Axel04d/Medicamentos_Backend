# medicamentos/schema.py

import graphene
from graphene_django import DjangoObjectType
from .models import Medicamento

class MedicamentoType(DjangoObjectType):
    class Meta:
        model = Medicamento

class Query(graphene.ObjectType):
    medicamentos = graphene.List(MedicamentoType)

    def resolve_medicamentos(self, info, **kwargs):
        return Medicamento.objects.all()

class CreateMedicamento(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    descripcion = graphene.String()
    enfermedad = graphene.String()

    class Arguments:
        nombre = graphene.String()
        descripcion = graphene.String()
        enfermedad = graphene.String()

    def mutate(self, info, nombre, descripcion, enfermedad):
        medicamento = Medicamento(nombre=nombre, descripcion=descripcion, enfermedad=enfermedad)
        medicamento.save()
        return CreateMedicamento(
            id=medicamento.id,
            nombre=medicamento.nombre,
            descripcion=medicamento.descripcion,
            enfermedad=medicamento.enfermedad,
        )

class Mutation(graphene.ObjectType):
    create_medicamento = CreateMedicamento.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
