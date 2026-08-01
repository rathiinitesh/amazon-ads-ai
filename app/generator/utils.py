import random

from faker import Faker

from app.generator.config import GeneratorConfig

fake = Faker()

random.seed(GeneratorConfig.RANDOM_SEED)
Faker.seed(GeneratorConfig.RANDOM_SEED)
