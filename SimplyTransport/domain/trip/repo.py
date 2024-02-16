from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .model import TripModel


class TripRepository(SQLAlchemyAsyncRepository[TripModel]):
    """Trip repository."""

    async def get_first_trips_by_route_ids(self, route_ids: list[str], direction: int) -> list[TripModel]:
        """Get first trips by route_ids."""

        result = await self.session.execute(
            select(TripModel)
            .where(TripModel.route_id.in_(route_ids))
            .where(TripModel.direction == direction)
            .distinct(TripModel.route_id)
        )
        return result.scalars().all()

    model_type = TripModel


async def provide_trip_repo(db_session: AsyncSession) -> TripRepository:
    """This provides the Trip repository."""

    return TripRepository(session=db_session)
