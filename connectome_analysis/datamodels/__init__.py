
import cache.serverobjcache
import cache.structurepositiondict
import queries

StructureCache = cache.serverobjcache.ServerObjCache(servergetfunc=queries._GetStructure)
StructureTypeCache = cache.serverobjcache.ServerObjCache(servergetfunc=queries._GetStructureType)

StructurePositionCache = cache.structurepositiondict.StructurePositionDict(servergetfunc=queries.GetStructureApproxPosition)
