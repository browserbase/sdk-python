# Changelog

## 1.5.0-alpha.0 (2025-09-05)

Full Changelog: [v1.4.0...v1.5.0-alpha.0](https://github.com/browserbase/sdk-python/compare/v1.4.0...v1.5.0-alpha.0)

### Features

* **api:** api update ([e94ddbd](https://github.com/browserbase/sdk-python/commit/e94ddbd8777b97d4e8ab193e1bf3eaad983ecec9))
* **api:** api update ([28115fb](https://github.com/browserbase/sdk-python/commit/28115fb584336dbf5b08043ad8f9cf1d911240ea))
* **api:** api update ([3209287](https://github.com/browserbase/sdk-python/commit/32092872a3d4d48824b4d77d517ffdb06470ad95))
* **api:** api update ([f38e029](https://github.com/browserbase/sdk-python/commit/f38e02981ae0777cb3d922845902b2673dc832fa))
* **api:** api update ([1d9f769](https://github.com/browserbase/sdk-python/commit/1d9f7694bc0d465ce758ddcec41359e9cd1a08ad))
* **api:** api update ([d72f39f](https://github.com/browserbase/sdk-python/commit/d72f39fbe29342cfc77e9b224f2ad0a5a77aaae4))
* **api:** api update ([6d449b3](https://github.com/browserbase/sdk-python/commit/6d449b3deb284a72528877a8729f4cf7a418275d))
* **api:** api update ([8bd5f8b](https://github.com/browserbase/sdk-python/commit/8bd5f8bcca3a2e5baadfc06009546692e63eb744))
* **api:** api update ([1ce99ef](https://github.com/browserbase/sdk-python/commit/1ce99efe89c1d0757ca3100cca8619faa4082f74))
* **api:** api update ([1cbb849](https://github.com/browserbase/sdk-python/commit/1cbb8498bf70c15c001f620b821519216cbadd97))
* **api:** manual updates ([5893fc6](https://github.com/browserbase/sdk-python/commit/5893fc6165cfd88378d6725317e30c7cb6faf8df))
* **api:** manual updates ([074f06d](https://github.com/browserbase/sdk-python/commit/074f06d0dfb08554229348828afd2cc1defe94ee))
* clean up environment call outs ([82c38c4](https://github.com/browserbase/sdk-python/commit/82c38c494a175c1b6b38bab3615916c30ba25d14))
* **client:** add follow_redirects request option ([a8b0b5e](https://github.com/browserbase/sdk-python/commit/a8b0b5e4c6445e0e8c0d3673a090aabab09a50fd))
* **client:** add support for aiohttp ([3516092](https://github.com/browserbase/sdk-python/commit/35160921e262f147cc723a754f14cfd9875603f5))
* **client:** support file upload requests ([2f338f0](https://github.com/browserbase/sdk-python/commit/2f338f009e556ef9be05f49816b17cef138bda17))
* improve future compat with pydantic v3 ([8b5256c](https://github.com/browserbase/sdk-python/commit/8b5256c801e1423a4daf6bf49de7509a32ebfde2))
* **types:** replace List[str] with SequenceNotStr in params ([55083f6](https://github.com/browserbase/sdk-python/commit/55083f678b68020fae835af5cd58e0e5deea2888))


### Bug Fixes

* avoid newer type syntax ([85f597b](https://github.com/browserbase/sdk-python/commit/85f597b34d149138f1b5afdc52062cb131e3a30a))
* **ci:** correct conditional ([a36b873](https://github.com/browserbase/sdk-python/commit/a36b87379b404613673720dd9f498ed76dfe5c3a))
* **ci:** release-doctor — report correct token name ([61b97ff](https://github.com/browserbase/sdk-python/commit/61b97fff5ea92bade293c5f5f4a84b0d991375e7))
* **client:** correctly parse binary response | stream ([9614c4c](https://github.com/browserbase/sdk-python/commit/9614c4c05bc57ea60100aec9a194aee7a39e701b))
* **client:** don't send Content-Type header on GET requests ([c4c4185](https://github.com/browserbase/sdk-python/commit/c4c4185de32b28c09565b6fe84efd65fd411abb9))
* fix extension types in playwright_extensions ([8b652e7](https://github.com/browserbase/sdk-python/commit/8b652e78be1493d03e13d2a116cbc6969a880e58))
* **parsing:** correctly handle nested discriminated unions ([d020678](https://github.com/browserbase/sdk-python/commit/d0206786894ecfb22e0924edb8a227414b17788d))
* **parsing:** ignore empty metadata ([118c4d4](https://github.com/browserbase/sdk-python/commit/118c4d41bda811d2d942793d8ab029b272c7a5c6))
* **parsing:** parse extra field types ([c7ef875](https://github.com/browserbase/sdk-python/commit/c7ef87549e324fb06fab945e1754ef7b56b30031))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e298407](https://github.com/browserbase/sdk-python/commit/e2984077537fd6dee0191329a083ad0ccf9fd76f))


### Chores

* **ci:** change upload type ([e42da7c](https://github.com/browserbase/sdk-python/commit/e42da7c1fed216ff2b15223c49f1111bc0ef16e5))
* **ci:** enable for pull requests ([03a6db7](https://github.com/browserbase/sdk-python/commit/03a6db72e98bf1606bf68928b2ac5029cba088df))
* **ci:** only run for pushes and fork pull requests ([c8cb51f](https://github.com/browserbase/sdk-python/commit/c8cb51f311f4d39863127fab189c95d84a186bc6))
* **docs:** grammar improvements ([f32a9e2](https://github.com/browserbase/sdk-python/commit/f32a9e258a9b0b4d29c24137d5a7207907f00f9b))
* **docs:** remove reference to rye shell ([07d129a](https://github.com/browserbase/sdk-python/commit/07d129a04211037d123b06d36347741960e75323))
* **docs:** remove unnecessary param examples ([62209dc](https://github.com/browserbase/sdk-python/commit/62209dcac034f40ac8b3b8a119e532201a227680))
* **internal:** add Sequence related utils ([34b0dd6](https://github.com/browserbase/sdk-python/commit/34b0dd6b4297fafc2bcb9e8243c8d3c2e2e435fc))
* **internal:** bump pinned h11 dep ([5e3270d](https://github.com/browserbase/sdk-python/commit/5e3270da2e4f41efdd345d073a42d6791eb22a84))
* **internal:** change ci workflow machines ([14c0ac4](https://github.com/browserbase/sdk-python/commit/14c0ac49a6d9d42f5401a5c24ddb8586b3998fb2))
* **internal:** codegen related update ([f979aff](https://github.com/browserbase/sdk-python/commit/f979aff605c0d74efb561e0b169ad39b486ab5a0))
* **internal:** codegen related update ([12de9f3](https://github.com/browserbase/sdk-python/commit/12de9f324fbb40bec91cd7c6b16af1440c4f7373))
* **internal:** codegen related update ([c4157cb](https://github.com/browserbase/sdk-python/commit/c4157cb8470b1d0ca67e6757f4fe9146a630cc82))
* **internal:** codegen related update ([ccb2c95](https://github.com/browserbase/sdk-python/commit/ccb2c95002bb6a38e1eb8b9a84e4a335d5ee1a13))
* **internal:** fix ruff target version ([e6a3df4](https://github.com/browserbase/sdk-python/commit/e6a3df40564b4ba3d23514e0b42221010d465bf6))
* **internal:** update comment in script ([a7aec17](https://github.com/browserbase/sdk-python/commit/a7aec17c02632684dfeb7759dd6a5322efe092ce))
* **internal:** update conftest.py ([5d3a2b1](https://github.com/browserbase/sdk-python/commit/5d3a2b1906ca5fca5c84c6d6684a8a62b6700479))
* **internal:** update pyright exclude list ([33ba4b4](https://github.com/browserbase/sdk-python/commit/33ba4b47ddeb8c0aa19a11f35a7cea9aa9a0966d))
* **package:** mark python 3.13 as supported ([2450b8e](https://github.com/browserbase/sdk-python/commit/2450b8eb2349adde689febd09269915d41e7a590))
* **project:** add settings file for vscode ([a406241](https://github.com/browserbase/sdk-python/commit/a4062413b2fce397d59ea9ceaec7ed0565880fe2))
* **readme:** fix version rendering on pypi ([a8afe1a](https://github.com/browserbase/sdk-python/commit/a8afe1a67c48080ef202cac88da9b5d59534799a))
* **readme:** update badges ([869a3f4](https://github.com/browserbase/sdk-python/commit/869a3f4dd7e6f19225b697aeee89ce98a2174c0a))
* **tests:** add tests for httpx client instantiation & proxies ([9c5d88c](https://github.com/browserbase/sdk-python/commit/9c5d88cb4cbbda5aa618cba2f5217bacd4a228cc))
* **tests:** run tests in parallel ([94308de](https://github.com/browserbase/sdk-python/commit/94308dea065f54268145b175a13e0dbfd2a9cc81))
* **tests:** skip some failing tests on the latest python versions ([7bc40f0](https://github.com/browserbase/sdk-python/commit/7bc40f068d290a479a0d4070ef54e8f8c4ef598d))
* update @stainless-api/prism-cli to v5.15.0 ([b48933b](https://github.com/browserbase/sdk-python/commit/b48933b2f68eafaa554662eb7f41bf960a74d8b6))
* update github action ([d57dc03](https://github.com/browserbase/sdk-python/commit/d57dc0398b083556ed7ceee265efcf282062005d))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([4bbda56](https://github.com/browserbase/sdk-python/commit/4bbda56cdb4adf677f67011f42f5c3e324a5f60e))

## 1.4.0 (2025-05-16)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/browserbase/sdk-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([d3b2ee1](https://github.com/browserbase/sdk-python/commit/d3b2ee1e3c69efbdcb2f0e53b4625e2c8a2a7430))


### Bug Fixes

* **package:** support direct resource imports ([8feb502](https://github.com/browserbase/sdk-python/commit/8feb502c7e73e8abed43afae5a0526282c4f0dfe))
* **pydantic v1:** more robust ModelField.annotation check ([5292730](https://github.com/browserbase/sdk-python/commit/5292730dd7b1585210d7ab8e640ed78a5dd9740a))


### Chores

* broadly detect json family of content-type headers ([ffe29f8](https://github.com/browserbase/sdk-python/commit/ffe29f8dc99d5e7462a0a9bbd488c368e836acdc))
* **ci:** add timeout thresholds for CI jobs ([3ca4458](https://github.com/browserbase/sdk-python/commit/3ca4458cf31650ce8749c56bee4549811cadec1f))
* **ci:** fix installation instructions ([99a7328](https://github.com/browserbase/sdk-python/commit/99a7328f22f6da3cd96d70b00c2a6fa0d4c82b37))
* **ci:** only use depot for staging repos ([646f7d8](https://github.com/browserbase/sdk-python/commit/646f7d832f269d383a0da5fe5732a52ec10787b2))
* **ci:** upload sdks to package manager ([ff18efd](https://github.com/browserbase/sdk-python/commit/ff18efdf051eabcb52863739942b652d86ed2231))
* **internal:** avoid errors for isinstance checks on proxies ([b33d222](https://github.com/browserbase/sdk-python/commit/b33d222fd5fdd6eaaca62fb6eb6d9f878a01d31d))
* **internal:** base client updates ([44f575e](https://github.com/browserbase/sdk-python/commit/44f575efd621315d9bd28e7921554980045af6ed))
* **internal:** bump pyright version ([bb6bbd3](https://github.com/browserbase/sdk-python/commit/bb6bbd36b3b0fb7595bcc6bd9b25c0aafd6a08af))
* **internal:** codegen related update ([9f4f8d1](https://github.com/browserbase/sdk-python/commit/9f4f8d1172d5c4b9fa36c8c97ab6e10958ff2959))
* **internal:** fix list file params ([74b3df7](https://github.com/browserbase/sdk-python/commit/74b3df7160585d981ff5390b6f354926188aaa2a))
* **internal:** import reformatting ([bba19e4](https://github.com/browserbase/sdk-python/commit/bba19e44eb67116740b27e1fea04abe06a97e4cd))
* **internal:** minor formatting changes ([0c58843](https://github.com/browserbase/sdk-python/commit/0c58843c75075e3803c9a5a9790f48558a78e712))
* **internal:** refactor retries to not use recursion ([4161fdb](https://github.com/browserbase/sdk-python/commit/4161fdbcf76a18deee8b790944369225fb4331ff))
* **internal:** update models test ([5e5dc11](https://github.com/browserbase/sdk-python/commit/5e5dc11c53c60164829b145762818545cfe36f52))

## 1.3.0 (2025-04-15)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/browserbase/sdk-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([#131](https://github.com/browserbase/sdk-python/issues/131)) ([1be828d](https://github.com/browserbase/sdk-python/commit/1be828d5c83e48af8740886303f73620bc71b1ba))
* **api:** api update ([#133](https://github.com/browserbase/sdk-python/issues/133)) ([2a08d98](https://github.com/browserbase/sdk-python/commit/2a08d98914d26cdc36d080bccebd66786b5247ff))
* **api:** api update ([#140](https://github.com/browserbase/sdk-python/issues/140)) ([134049e](https://github.com/browserbase/sdk-python/commit/134049e29ba480a2238a08c327070bda96b05109))
* **api:** api update ([#141](https://github.com/browserbase/sdk-python/issues/141)) ([145e5cb](https://github.com/browserbase/sdk-python/commit/145e5cbfc76ac2731b1d6eb3c069cba59a9fbcd9))
* **api:** api update ([#143](https://github.com/browserbase/sdk-python/issues/143)) ([d55e411](https://github.com/browserbase/sdk-python/commit/d55e4118972d7badbe09a2dd46257d2e66822b85))
* **client:** allow passing `NotGiven` for body ([#125](https://github.com/browserbase/sdk-python/issues/125)) ([6cdee1b](https://github.com/browserbase/sdk-python/commit/6cdee1ba5775d3c72e0cbd9fe757a1b7452780bd))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#123](https://github.com/browserbase/sdk-python/issues/123)) ([c8b2cd7](https://github.com/browserbase/sdk-python/commit/c8b2cd77f4cb07d06a00a09cac3eaa55cf6c6925))
* **ci:** ensure pip is always available ([#138](https://github.com/browserbase/sdk-python/issues/138)) ([173fdde](https://github.com/browserbase/sdk-python/commit/173fddeea8867f93428bddc5ab1d9e1fcd5a925e))
* **ci:** remove publishing patch ([#139](https://github.com/browserbase/sdk-python/issues/139)) ([bd66d56](https://github.com/browserbase/sdk-python/commit/bd66d56eec53a7778ca624a7ccd00fcf8a9f69af))
* **client:** mark some request bodies as optional ([6cdee1b](https://github.com/browserbase/sdk-python/commit/6cdee1ba5775d3c72e0cbd9fe757a1b7452780bd))
* **perf:** optimize some hot paths ([042f048](https://github.com/browserbase/sdk-python/commit/042f048847634ed606d475a0aaeedc5fd129ddbd))
* **perf:** skip traversing types for NotGiven values ([5cc6c58](https://github.com/browserbase/sdk-python/commit/5cc6c58561556e2b50fccbeed5e123adf3aba72d))
* **types:** handle more discriminated union shapes ([#137](https://github.com/browserbase/sdk-python/issues/137)) ([d9e09e3](https://github.com/browserbase/sdk-python/commit/d9e09e3d2428a92c29a4411533564637ce5b3121))


### Chores

* **client:** minor internal fixes ([47df6f5](https://github.com/browserbase/sdk-python/commit/47df6f5956507649f684df46bf2b5bb18aa7bc93))
* **docs:** update client docstring ([#129](https://github.com/browserbase/sdk-python/issues/129)) ([b2201f1](https://github.com/browserbase/sdk-python/commit/b2201f1d9f99f67a3b8fa21ba19560e72a245611))
* fix typos ([#142](https://github.com/browserbase/sdk-python/issues/142)) ([0157632](https://github.com/browserbase/sdk-python/commit/015763281689247799dd97e46884ba3be520c2f5))
* **internal:** bump rye to 0.44.0 ([#136](https://github.com/browserbase/sdk-python/issues/136)) ([9aeac01](https://github.com/browserbase/sdk-python/commit/9aeac01a20df8303f806e22b274bdd10adaeea49))
* **internal:** codegen related update ([#124](https://github.com/browserbase/sdk-python/issues/124)) ([0678102](https://github.com/browserbase/sdk-python/commit/0678102eee40182b0fc2c2a2b2e3f965a2885a50))
* **internal:** codegen related update ([#132](https://github.com/browserbase/sdk-python/issues/132)) ([3248d7e](https://github.com/browserbase/sdk-python/commit/3248d7e6242808bcb74427cb1b78ac52dee0948c))
* **internal:** expand CI branch coverage ([4494839](https://github.com/browserbase/sdk-python/commit/449483977d4af8b56b916d555bea966f25304ac7))
* **internal:** fix devcontainers setup ([#126](https://github.com/browserbase/sdk-python/issues/126)) ([eaf577b](https://github.com/browserbase/sdk-python/commit/eaf577b05bd72e2bb40105131a65e7c13172c3bb))
* **internal:** properly set __pydantic_private__ ([#127](https://github.com/browserbase/sdk-python/issues/127)) ([5236106](https://github.com/browserbase/sdk-python/commit/52361065d4547b06c44a07396e0679f588181053))
* **internal:** reduce CI branch coverage ([1bd4d8b](https://github.com/browserbase/sdk-python/commit/1bd4d8bf088ac47c01a12048cb7b3c963d18eb4a))
* **internal:** remove extra empty newlines ([#134](https://github.com/browserbase/sdk-python/issues/134)) ([2206050](https://github.com/browserbase/sdk-python/commit/22060504e0f57402decfff129778a472717e29e1))
* **internal:** remove trailing character ([#145](https://github.com/browserbase/sdk-python/issues/145)) ([2b055d7](https://github.com/browserbase/sdk-python/commit/2b055d730b2313227a0193cfc2b95056d4731464))
* **internal:** remove unused http client options forwarding ([#130](https://github.com/browserbase/sdk-python/issues/130)) ([c63a3bd](https://github.com/browserbase/sdk-python/commit/c63a3bdad3f35658d87d48bbd5e746a36228a8ab))
* **internal:** slight transform perf improvement ([#147](https://github.com/browserbase/sdk-python/issues/147)) ([2d46582](https://github.com/browserbase/sdk-python/commit/2d46582e5bb55d3ca74c2a4191144743d5f0058b))
* **internal:** update client tests ([#121](https://github.com/browserbase/sdk-python/issues/121)) ([862cd7e](https://github.com/browserbase/sdk-python/commit/862cd7efb4c694866ab385c5a70fd450b917f057))
* **internal:** update pyright settings ([0f0e110](https://github.com/browserbase/sdk-python/commit/0f0e110388f893b86881aa67badc30af8e271b8a))
* slight wording improvement in README ([#148](https://github.com/browserbase/sdk-python/issues/148)) ([c40603c](https://github.com/browserbase/sdk-python/commit/c40603cafa809128edeff23eca37db97dda8de54))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#128](https://github.com/browserbase/sdk-python/issues/128)) ([5e2932f](https://github.com/browserbase/sdk-python/commit/5e2932f5c13c19eb454116ffdce38863556feaf1))

## 1.2.0 (2025-02-11)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/browserbase/sdk-python/compare/v1.1.0...v1.2.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#117](https://github.com/browserbase/sdk-python/issues/117)) ([e53c47a](https://github.com/browserbase/sdk-python/commit/e53c47ae14f4dca507cc146b37b81d5e59845806))


### Chores

* **internal:** bummp ruff dependency ([#115](https://github.com/browserbase/sdk-python/issues/115)) ([f687590](https://github.com/browserbase/sdk-python/commit/f68759062445e8336ca0f6c9b0bde3b0d2ca1e62))
* **internal:** change default timeout to an int ([#113](https://github.com/browserbase/sdk-python/issues/113)) ([081bb21](https://github.com/browserbase/sdk-python/commit/081bb216f4b9a4df0dfdd51bcbcacef0154fe636))
* **internal:** fix type traversing dictionary params ([#118](https://github.com/browserbase/sdk-python/issues/118)) ([cc59fe8](https://github.com/browserbase/sdk-python/commit/cc59fe8950fa4e66ee5efd598b69da9c0c8f08a0))
* **internal:** minor type handling changes ([#119](https://github.com/browserbase/sdk-python/issues/119)) ([7be3940](https://github.com/browserbase/sdk-python/commit/7be3940cfb0bb947a6774ec225b5eb450a951e88))

## 1.1.0 (2025-01-28)

Full Changelog: [v1.0.5...v1.1.0](https://github.com/browserbase/sdk-python/compare/v1.0.5...v1.1.0)

### Features

* **api:** api update ([#101](https://github.com/browserbase/sdk-python/issues/101)) ([5be14e9](https://github.com/browserbase/sdk-python/commit/5be14e9b49b95daa2bc043ed8c33b2d4527a7361))
* **api:** api update ([#104](https://github.com/browserbase/sdk-python/issues/104)) ([c13b2f9](https://github.com/browserbase/sdk-python/commit/c13b2f95924c940deece1f6e3b1e4ca2dfbd9fe7))
* **api:** api update ([#105](https://github.com/browserbase/sdk-python/issues/105)) ([fc3b82f](https://github.com/browserbase/sdk-python/commit/fc3b82f224e92e273d484f8b0f52eb433210e38b))
* **api:** api update ([#109](https://github.com/browserbase/sdk-python/issues/109)) ([faca7e9](https://github.com/browserbase/sdk-python/commit/faca7e94c6086d461b81f2806868af2e1506e035))
* **api:** api update ([#111](https://github.com/browserbase/sdk-python/issues/111)) ([42ae774](https://github.com/browserbase/sdk-python/commit/42ae77474c2fbe9eefd9929e15d8d51cbf40bc00))


### Bug Fixes

* **client:** only call .close() when needed ([#97](https://github.com/browserbase/sdk-python/issues/97)) ([01d5bd5](https://github.com/browserbase/sdk-python/commit/01d5bd5eb7675fc069fe01e7651d769df182270a))
* correctly handle deserialising `cls` fields ([#100](https://github.com/browserbase/sdk-python/issues/100)) ([b617b85](https://github.com/browserbase/sdk-python/commit/b617b85ef3cce3c16e38125bec483c72bc3d43c0))


### Chores

* add missing isclass check ([#94](https://github.com/browserbase/sdk-python/issues/94)) ([de5856d](https://github.com/browserbase/sdk-python/commit/de5856dac77567813f681615bef7d147e505a6a0))
* **internal:** add support for TypeAliasType ([#85](https://github.com/browserbase/sdk-python/issues/85)) ([64448c6](https://github.com/browserbase/sdk-python/commit/64448c6e020aaeb4b39b7ec8f1b28a6b8f0c746a))
* **internal:** bump httpx dependency ([#95](https://github.com/browserbase/sdk-python/issues/95)) ([d592266](https://github.com/browserbase/sdk-python/commit/d592266e85c40d14e4929089f8ae4db814d04ce7))
* **internal:** bump pydantic dependency ([#81](https://github.com/browserbase/sdk-python/issues/81)) ([e35a0d8](https://github.com/browserbase/sdk-python/commit/e35a0d85ef0e45aed1a5f58757427bf7c16a76f5))
* **internal:** bump pyright ([#83](https://github.com/browserbase/sdk-python/issues/83)) ([894b4c4](https://github.com/browserbase/sdk-python/commit/894b4c45b0c36963822923535391aa34dbfec766))
* **internal:** codegen related update ([#102](https://github.com/browserbase/sdk-python/issues/102)) ([f648bbb](https://github.com/browserbase/sdk-python/commit/f648bbbae4520a1003ecaf5cbd299da9aabfb90f))
* **internal:** codegen related update ([#106](https://github.com/browserbase/sdk-python/issues/106)) ([3fc9cde](https://github.com/browserbase/sdk-python/commit/3fc9cde212c1ea7f1010c9e688bd75841d828ace))
* **internal:** codegen related update ([#107](https://github.com/browserbase/sdk-python/issues/107)) ([c97e138](https://github.com/browserbase/sdk-python/commit/c97e1383ac673d05861653c0818c1d1c5b0fa5c8))
* **internal:** codegen related update ([#86](https://github.com/browserbase/sdk-python/issues/86)) ([ab76578](https://github.com/browserbase/sdk-python/commit/ab76578bdce5eba2410b09f497758fbf0e0d8cf0))
* **internal:** codegen related update ([#87](https://github.com/browserbase/sdk-python/issues/87)) ([f7f189e](https://github.com/browserbase/sdk-python/commit/f7f189ec317394f2fc532b8f95c3d15304298027))
* **internal:** codegen related update ([#88](https://github.com/browserbase/sdk-python/issues/88)) ([85f1492](https://github.com/browserbase/sdk-python/commit/85f1492efc58d86ebc34511ca1269a0db2a4d223))
* **internal:** codegen related update ([#93](https://github.com/browserbase/sdk-python/issues/93)) ([57f0977](https://github.com/browserbase/sdk-python/commit/57f0977c8e050b85b2c2de91202f6775299f80bf))
* **internal:** codegen related update ([#99](https://github.com/browserbase/sdk-python/issues/99)) ([f817bcb](https://github.com/browserbase/sdk-python/commit/f817bcb67c2080a954c476c15dc048c2c628243a))
* **internal:** fix some typos ([#92](https://github.com/browserbase/sdk-python/issues/92)) ([51d9f42](https://github.com/browserbase/sdk-python/commit/51d9f42a32d17d2d2277eb8a7b8f35a980c7c485))
* **internal:** minor formatting changes ([#110](https://github.com/browserbase/sdk-python/issues/110)) ([195c595](https://github.com/browserbase/sdk-python/commit/195c595bfbe2ed97ae4b551658618f4a99a255f0))
* **internal:** remove some duplicated imports ([#89](https://github.com/browserbase/sdk-python/issues/89)) ([a82ae7d](https://github.com/browserbase/sdk-python/commit/a82ae7d418b1daf68c85e70dea61e628eb785b79))
* **internal:** updated imports ([#90](https://github.com/browserbase/sdk-python/issues/90)) ([dc6e187](https://github.com/browserbase/sdk-python/commit/dc6e187bfe9585692b2de1b67fc83f027a52c43c))
* make the `Omit` type public ([#78](https://github.com/browserbase/sdk-python/issues/78)) ([a7bdc57](https://github.com/browserbase/sdk-python/commit/a7bdc57ab7f327da61121986ba7b006238d0e5b5))


### Documentation

* fix typos ([#98](https://github.com/browserbase/sdk-python/issues/98)) ([d4f4bae](https://github.com/browserbase/sdk-python/commit/d4f4bae46341e91ac537e121bba38e511c7026bc))
* **readme:** example snippet for client context manager ([#91](https://github.com/browserbase/sdk-python/issues/91)) ([950c8af](https://github.com/browserbase/sdk-python/commit/950c8af19db4581fabd5b965ca4f0af3cc5cd6dc))
* **readme:** fix http client proxies example ([#82](https://github.com/browserbase/sdk-python/issues/82)) ([cc67c77](https://github.com/browserbase/sdk-python/commit/cc67c773b11b42b406b677f466c7c0ef090b254e))

## 1.0.5 (2024-12-03)

Full Changelog: [v1.0.4...v1.0.5](https://github.com/browserbase/sdk-python/compare/v1.0.4...v1.0.5)

### Chores

* **internal:** bump pyright ([#73](https://github.com/browserbase/sdk-python/issues/73)) ([d5f9711](https://github.com/browserbase/sdk-python/commit/d5f97119b2ec2334f47029541173e78ca846abae))

## 1.0.4 (2024-11-29)

Full Changelog: [v1.0.3...v1.0.4](https://github.com/browserbase/sdk-python/compare/v1.0.3...v1.0.4)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#71](https://github.com/browserbase/sdk-python/issues/71)) ([7b87947](https://github.com/browserbase/sdk-python/commit/7b87947d0cdf555c73a1527b3e396cd40175d0b4))


### Chores

* **internal:** codegen related update ([#68](https://github.com/browserbase/sdk-python/issues/68)) ([3e4372e](https://github.com/browserbase/sdk-python/commit/3e4372ed8790e32850e1196c402e0023cd8a0f9d))
* **internal:** exclude mypy from running on tests ([#70](https://github.com/browserbase/sdk-python/issues/70)) ([edd3628](https://github.com/browserbase/sdk-python/commit/edd3628710ed8f863bce5df336385dd6d380041e))

## 1.0.3 (2024-11-22)

Full Changelog: [v1.0.2...v1.0.3](https://github.com/browserbase/sdk-python/compare/v1.0.2...v1.0.3)

### Chores

* **internal:** fix compat model_dump method when warnings are passed ([#65](https://github.com/browserbase/sdk-python/issues/65)) ([4e999de](https://github.com/browserbase/sdk-python/commit/4e999de99372f6b348e74aa37663dd809c5d0da7))

## 1.0.2 (2024-11-19)

Full Changelog: [v1.0.1...v1.0.2](https://github.com/browserbase/sdk-python/compare/v1.0.1...v1.0.2)

### Chores

* rebuild project due to codegen change ([#59](https://github.com/browserbase/sdk-python/issues/59)) ([bd52098](https://github.com/browserbase/sdk-python/commit/bd520989c50f8353c7184930d0da661bdc8625fa))

## 1.0.1 (2024-11-18)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/browserbase/sdk-python/compare/v1.0.0...v1.0.1)

### Features

* **api:** api update ([#48](https://github.com/browserbase/sdk-python/issues/48)) ([b17a3b8](https://github.com/browserbase/sdk-python/commit/b17a3b8e6984447421a7581ca56c0521cb3b55dd))
* **api:** api update ([#51](https://github.com/browserbase/sdk-python/issues/51)) ([dc2da25](https://github.com/browserbase/sdk-python/commit/dc2da25d2e33d55e5655cbb8000fd4afdd6bbf62))


### Chores

* rebuild project due to codegen change ([#53](https://github.com/browserbase/sdk-python/issues/53)) ([b1684fa](https://github.com/browserbase/sdk-python/commit/b1684fa889aecf2fe7965a37ebd9c73977136ef6))
* rebuild project due to codegen change ([#54](https://github.com/browserbase/sdk-python/issues/54)) ([e6a41da](https://github.com/browserbase/sdk-python/commit/e6a41dab6f0de6894a97067611166b1bc61893a2))
* rebuild project due to codegen change ([#55](https://github.com/browserbase/sdk-python/issues/55)) ([ff17087](https://github.com/browserbase/sdk-python/commit/ff1708757bdeaa4e6b8d1959d1830105bd7f4b92))
* rebuild project due to codegen change ([#57](https://github.com/browserbase/sdk-python/issues/57)) ([dfd0e19](https://github.com/browserbase/sdk-python/commit/dfd0e199c2447d4bd1b6704745d22f959a6b6bb1))
* rebuild project due to codegen change ([#58](https://github.com/browserbase/sdk-python/issues/58)) ([f3be0be](https://github.com/browserbase/sdk-python/commit/f3be0bec13d95c65ab4cc81565b456cb566a62e2))

## 1.0.0 (2024-10-29)

Full Changelog: [v1.0.0-alpha.0...v1.0.0](https://github.com/browserbase/sdk-python/compare/v1.0.0-alpha.0...v1.0.0)

### Features

* **api:** api update ([#44](https://github.com/browserbase/sdk-python/issues/44)) ([46621f6](https://github.com/browserbase/sdk-python/commit/46621f6cf67f2c30b52a5dfcfbaa36c80053e0cf))

## 1.0.0-alpha.0 (2024-10-29)

Full Changelog: [v0.1.0-alpha.7...v1.0.0-alpha.0](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.7...v1.0.0-alpha.0)

### Features

* **api:** api update ([#39](https://github.com/browserbase/sdk-python/issues/39)) ([8c98d9e](https://github.com/browserbase/sdk-python/commit/8c98d9e9da61daba527262aa1b0a1334da22a596))
* **api:** api update ([#41](https://github.com/browserbase/sdk-python/issues/41)) ([0557ee5](https://github.com/browserbase/sdk-python/commit/0557ee507fc35faa9aabd8d06ce8047bb07843aa))

## 0.1.0-alpha.7 (2024-10-28)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([#35](https://github.com/browserbase/sdk-python/issues/35)) ([c694662](https://github.com/browserbase/sdk-python/commit/c69466218e105b524b4ad98208283b96eccf056d))

## 0.1.0-alpha.6 (2024-10-28)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([#32](https://github.com/browserbase/sdk-python/issues/32)) ([a956d94](https://github.com/browserbase/sdk-python/commit/a956d9415cadd959c1a40a86d64117ffe5812e48))

## 0.1.0-alpha.5 (2024-10-28)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([#27](https://github.com/browserbase/sdk-python/issues/27)) ([3050f62](https://github.com/browserbase/sdk-python/commit/3050f628fde93180fe9f5bd6c6d6eac511a2624c))
* **api:** update via SDK Studio ([#28](https://github.com/browserbase/sdk-python/issues/28)) ([b5f5482](https://github.com/browserbase/sdk-python/commit/b5f5482f57e27d38af4ac550845d5484f870bf39))
* **api:** update via SDK Studio ([#29](https://github.com/browserbase/sdk-python/issues/29)) ([fc40b62](https://github.com/browserbase/sdk-python/commit/fc40b62e7dbe6af78e429cb1d4cc090f3cf75286))
* various codegen changes ([ebb2283](https://github.com/browserbase/sdk-python/commit/ebb2283beb1651cf679774e4cfe45e652118f0e8))

## 0.1.0-alpha.4 (2024-10-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#16](https://github.com/browserbase/sdk-python/issues/16)) ([78347f5](https://github.com/browserbase/sdk-python/commit/78347f5f2a251eca20ffeb1e5d78ee843ce74415))
* **api:** update via SDK Studio ([#18](https://github.com/browserbase/sdk-python/issues/18)) ([b958c13](https://github.com/browserbase/sdk-python/commit/b958c13c01fd9f0cedbb5723ee54574ad769b539))
* **api:** update via SDK Studio ([#19](https://github.com/browserbase/sdk-python/issues/19)) ([90ea00d](https://github.com/browserbase/sdk-python/commit/90ea00def3c88ff0b1a6d71b65abd155b230e2c0))
* **api:** update via SDK Studio ([#20](https://github.com/browserbase/sdk-python/issues/20)) ([0b9561f](https://github.com/browserbase/sdk-python/commit/0b9561f5c8a91ea372ab68d5679e05e255f302c7))
* **api:** update via SDK Studio ([#21](https://github.com/browserbase/sdk-python/issues/21)) ([00b8c8b](https://github.com/browserbase/sdk-python/commit/00b8c8be7b5bdf9fbe8da6410cf7dd2d002ad21e))

## 0.1.0-alpha.3 (2024-10-26)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#13](https://github.com/browserbase/sdk-python/issues/13)) ([ec90079](https://github.com/browserbase/sdk-python/commit/ec900790bd56f92b174304bb227461a65209cbdb))

## 0.1.0-alpha.2 (2024-10-26)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/browserbase/sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#10](https://github.com/browserbase/sdk-python/issues/10)) ([d33635f](https://github.com/browserbase/sdk-python/commit/d33635ff54944daeb6dff57fa901d1703a289bbc))

## 0.1.0-alpha.1 (2024-10-25)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/browserbase/sdk-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#7](https://github.com/browserbase/sdk-python/issues/7)) ([30c7100](https://github.com/browserbase/sdk-python/commit/30c71000404a55a64140d1f269220f2762aa5753))

## 0.0.1-alpha.1 (2024-10-25)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/browserbase/sdk-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* update SDK settings ([#1](https://github.com/browserbase/sdk-python/issues/1)) ([dc1e229](https://github.com/browserbase/sdk-python/commit/dc1e229189470b0f3df3c5a2e7da4e789fc76279))
