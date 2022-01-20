keywordsDict = {
    # Annotations_Java API
    'override': 'Annotation Java API',
    'suppresswarnings': 'Annotation Java API',
    'safevarargs': 'Annotation Java API',
    'functionalinterface': 'Annotation Java API',

    # Annotations_Spring
    'Autowired ': 'Annotation External',
    'Qualifier ': 'Annotation External',
    'Required ': 'Annotation External',
    'Value ': 'Annotation External',
    'Bean ': 'Annotation External',
    'ComponentScan ': 'Annotation External',
    'Configuration ': 'Annotation External',
    'Lazy ': 'Annotation External',
    'Component ': 'Annotation External',
    'Repository ': 'Annotation External',
    'Service ': 'Annotation External',
    'Controller ': 'Annotation External',
    'RequestMapping ': 'Annotation External',
    'CookieValue ': 'Annotation External',
    'CrossOrigin ': 'Annotation External',
    'ControllerAdvice ': 'Annotation External',
    'DeleteMapping ': 'Annotation External',
    'ExceptionHandler ': 'Annotation External',
    'GetMapping ': 'Annotation External',
    'InitBinder ': 'Annotation External',
    'Mapping ': 'Annotation External',
    'MatrixVariable ': 'Annotation External',
    'PatchMapping ': 'Annotation External',
    'PathVariable ': 'Annotation External',
    'PostMapping ': 'Annotation External',
    'PutMapping ': 'Annotation External',
    'RequestAttribute ': 'Annotation External',
    'RequestBody ': 'Annotation External',
    'RequestHeader ': 'Annotation External',
    'RequestParam ': 'Annotation External',
    'RequestPart ': 'Annotation External',
    'ResponseBody ': 'Annotation External',
    'ResponseStatus ': 'Annotation External',
    'RestController ': 'Annotation External',
    'RestControllerAdvice ': 'Annotation External',
    'SessionAttribute ': 'Annotation External',
    'SessionAttributes ': 'Annotation External',
    'Transactional ': 'Annotation External',
    'Cacheable ': 'Annotation External',
    'CacheConfig ': 'Annotation External',
    'CacheEvict ': 'Annotation External',
    'CachePut ': 'Annotation External',
    'Scheduled ': 'Annotation External',
    'Async ': 'Annotation External',
    'EnableAutoConfiguration ': 'Annotation External',
    'SpringBootApplication ': 'Annotation External',
    'EnableConfigServer ': 'Annotation External',
    'EnableEurekaServer ': 'Annotation External',
    'EnableDiscoveryClient ': 'Annotation External',
    'EnableCircuitBreaker ': 'Annotation External',
    'HystrixCommand ': 'Annotation External',

    # Exceptions

    # Collections
    'java.util.ArrayList': 'Collections Java API',
    'java.util.Vector': 'Collections Java API',
    'java.util.LinkedList': 'Collections Java API',
    'java.util.Stack': 'Collections Java API',
    'java.util.HashSet': 'Collections Java API',
    'java.util.TreeSet': 'Collections Java API',
    'java.util.HashMap': 'Collections Java API',
    'java.util.HashTable': 'Collections Java API',
    'java.util.TreeMap': 'Collections Java API',
    'java.util.Properties': 'Collections Java API',

    # Collections Related
    'java.util.Iterator': 'Collections Related Java API',
    'java.util.ListIterator': 'Collections Related Java API',
    'java.util.Enumeration': 'Collections Related Java API',
    'java.util.Comparator': 'Collections Related Java API',

    #

}

repoDict = {
    # Popular Open Source Projects Using Spring Framework

    # Proper size
    'generator-jhipster': 'jhipster',
    'kafdrop': 'obsidiandynamics',
    'sagan': 'spring-io',
    'TelegramBots': 'rubenlagus',
    'cwa-server': 'corona-warn-app',
    'spring-boot-admin': 'codecentric',

    # # Too big to be included
    # 'flowable-engine': 'flowable',
    # 'thingsboard': 'thingsboard',
    # 'cas': 'apereo',
    # 'uaa': 'cloudfoundry',
    # 'BroadleafCommerce': 'BroadleafCommerce',
    # 'shopizer': 'shopizer-ecommerce',
    # 'conductor': 'Netflix',
    # 'zipkin': 'openzipkin',
    # 'initializr': 'spring-io',
    # 'piggymetrics': 'sqshq',
    # 'spring-petclinic': 'spring-projects',

    # Woowacourse Projects

    # +50 stars
    '2021-jujeol-jujeol': 'woowacourse-teams',
    '2021-botobo': 'woowacourse-teams',
    '2021-pick-git': 'woowacourse-teams',
    '2021-darass': 'woowacourse-teams',
    '2020-doran-doran': 'woowacourse-teams',
    '2020-6rinkers': 'woowacourse-teams',

    # # others
    # '2021-tyf': 'woowacourse-teams',
    # '2021-drop-the-code': 'woowacourse-teams',
    # '2021-zzimkkong': 'woowacourse-teams',
    # '2021-babble': 'woowacourse-teams',
    # '2021-gpu-is-mine': 'woowacourse-teams',
    # '2021-cvi': 'woowacourse-teams',
    # '2021-nolto': 'woowacourse-teams',
    # '2021-see-you-there': 'woowacourse-teams',
    # '2020-taggle': 'woowacourse-teams',
    # '2020-legeno-around-here': 'woowacourse-teams',
    # '2020-saebyeok': 'woowacourse-teams',
    # '2020-devbie': 'woowacourse-teams',
    # '2020-zeze': 'woowacourse-teams',
    # '2020-14f-guys': 'woowacourse-teams',
    # '2020-songpa-people': 'woowacourse-teams',
    # '2020-seller-lee-company': 'woowacourse-teams',
}

# Scraping Completion Time Calculation
estimatedTime = len(repoDict.keys()) * len(keywordsDict.keys()) * 15
