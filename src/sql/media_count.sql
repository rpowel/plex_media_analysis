SELECT
    case
        when metadata_type = 1 then 'Movies'
        when metadata_type = 2 then 'TV Shows'
        when metadata_type = 3 then 'Seasons'
        when metadata_type = 4 then 'Episodes'
        when metadata_type = 8 then 'Artists'
        when metadata_type = 9 then 'Albums'
        when metadata_type = 10 then 'Tracks'
        when metadata_type = 12 then 'Prerolls and Trailers'
        when metadata_type = 13 then 'Pictures'
        when metadata_type = 14 then 'Picture Folders'
        when metadata_type = 15 then 'Playlists'
        when metadata_type = 18 then 'Collections'
        when metadata_type = 42 then 'Plex Background Info'
    end as 'Media Type',
    count(*) as 'N'
from metadata_items
group by metadata_type
ORDER BY "N" DESC;
