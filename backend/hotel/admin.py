from django.contrib import admin

from .models import HotelRooms, HotelFields, RatingsRooms, BookingRoom


class HotelFieldsAdmin(admin.StackedInline):
    model = HotelFields
    extra = 1
    show_change_link = True


class RatingsRoomsAdmin(admin.StackedInline):
    model = RatingsRooms
    extra = 1
    show_change_link = True


@admin.register(HotelRooms)
class HotelRoomsAdmin(admin.ModelAdmin):
    """Hotel room"""
    list_display = ("title", "desc")
    search_fields = ("title",)
    inlines = [HotelFieldsAdmin, RatingsRoomsAdmin]


@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    """Booking room"""
    list_display = ("name", "phone", "entry_date", "depart_date", "adult", "children")
    search_fields = ("name",)

