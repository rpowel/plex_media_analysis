SELECT
    metadata_items.id,
    metadata_items.library_section_id,
    parent_id,
    CASE
        WHEN metadata_type = 1 THEN 'Movie'
        WHEN metadata_type = 2 THEN 'TV Show'
        WHEN metadata_type = 3 THEN 'Season'
        WHEN metadata_type = 4 THEN 'Episode'
        WHEN metadata_type = 8 THEN 'Artist'
        WHEN metadata_type = 9 THEN 'Album'
        WHEN metadata_type = 10 THEN 'Track'
        ELSE 'NA'
    END AS type,
    title,
    tagline,
    summary,
    mi.duration as duration,
    mi.size,
    mi.container,
    originally_available_at AS available_date,
    year
FROM metadata_items
LEFT JOIN media_items mi ON metadata_items.id = mi.metadata_item_id
WHERE type != 'NA';
