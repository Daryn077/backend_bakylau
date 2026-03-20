import asyncio

from data_access.db.session import AsyncSessionLocal
from data_access.db.models.laboratory import Laboratory
from data_access.db.models.researcher import Researcher


async def seed():
    async with AsyncSessionLocal() as session:
        lab1 = Laboratory(
            name="Politeh",
            specialization="IS",
            university_id=1
        )
        lab1.researchers = [
            Researcher(full_name="Zhakiya Tlegen", degree="student"),
            Researcher(full_name="Sovet Merei", degree="student"),
        ]

        lab2 = Laboratory(
            name="KMU",
            specialization="IT med",
            university_id=2
        )
        lab2.researchers = [
            Researcher(full_name="Kerimbek Damir", degree="student"),
        ]

        session.add_all([lab1, lab2])
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())